# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from .entidades import Articulo, Categoria, db_connect, create_table
import logging
from string import capwords

"""class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
"""
class GuardarArticulosPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        articulo = Articulo()
        articulo.nombre = capwords(item["nombre"][0])
        articulo.precio = item["precio"][0]
        articulo.url = item["url"][0]
        articulo.categoria = item["categoria"][0]

        # check whether the author exists
        existe_categ = session.query(Categoria).filter_by(nombre=item["categoria"][0]).first()
        if existe_categ is not None:  # the current author exists
            articulo.categoria = existe_categ.id
        else:
            articulo.categoria = 1


        try:
            session.add(articulo)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item


class DuplicadosPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****DuplicatesPipeline: database connected****")

    def process_item(self, item, spider):
        cambios = False
        session = self.Session()
        art = session.query(Articulo).filter_by(nombre=capwords(item["nombre"][0])).first()
        if art is not None:  # the current quote exists
            if art.precio != item["precio"][0] or art.url != item["url"][0]:
                art.precio = item["precio"][0]
                art.url = item["url"][0]
                cambios = True

            cat = session.query(Categoria).filter_by(nombre=capwords(item["categoria"][0])).first()
            if cat is not None:
                if art.categoria != cat.id:
                    art.categoria = cat.id
                    cambios = True
            else:
                art.categoria = 1
                cambios = True

            if cambios:
                session.commit()
                session.close()
                raise DropItem("Se ha actualizado el articulo: %s" % item["nombre"][0])

            else:
                session.close()
                raise DropItem("El articulo %s se encuentra actualizado" % item["nombre"][0])

        else:
            session.close()
            return item

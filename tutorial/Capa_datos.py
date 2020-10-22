from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tutorial.tutorial.entidades import Base, Categoria, Articulo


class ArticulosData(object):

    def __init__(self):
        engine = create_engine('sqlite:///tutorial/scrapy_datos.db', echo=True)
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def getArtById(self, artId):
        """
        Devuelve un articulo, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Articulo
        """
        try:
            articulo = self.session.query(Articulo).filter_by(id=artId).first()
            return articulo
        except:
            return None

    def getAllArts(self):
        """
        Devuelve listado de todos los articulos.
        :rtype: list
        """
        articulos = self.session.query(Articulo).all()

        return articulos

    def getArtsByCat(self, catId):
        """
        Devuelve un listado de articulos, dado su id de categoria.
        Devuelve None si no encuentra nada.
        :rtype: list
        """
        try:
            articulos = self.session.query(Articulo).filter_by(categoria=catId).all()
            return articulos
        except:
            return None


    def getArtsTable(self):
        """
        Devuelve un articulo, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: list
        """
        try:
            articulos = self.session.query(
                Articulo, Categoria,
            ).filter(
                Articulo.categoria == Categoria.id,
            ).all()
            return articulos
        except:
            return None



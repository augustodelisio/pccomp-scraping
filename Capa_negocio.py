import webbrowser
from tutorial.tutorial.entidades import Articulo, Categoria, TablaArticulo
from tutorial.Capa_datos import ArticulosData

class ArticulosBusiness(object):

    def __init__(self):
        self.articulos = ArticulosData()


    def openweb(link):
        webbrowser.open(link, new=1)


    def getArtById(self, artId):
        """
        Devuelve un articulo, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Articulo
        """
        return self.articulos.getArtById(artId)


    def getArtsTable(self):
        """
        Devuelve un articulo, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: list
        """
        return self.articulos.getArtsTable()

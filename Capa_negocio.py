import webbrowser
from Capa_datos import DatosProducto


class NegocioProducto(object):

    def __init__(self):
        self.datos = DatosProducto()


    def openweb(link):
        webbrowser.open(link, new=1)


    def buscarProducto(filtro, entrada):
        if filtro == "Producto":
            return self.datos.buscarProducto(entrada.lower())
        elif filtro == "Categoria":
            return self.datos.buscarCategoria(entrada.lower())
        elif filtro == "Mayor precio":
            return self.datos.buscarMayorPrecio(entrada.lower())
        elif filtro == "Menor precio":
            return self.datos.buscarMenorPrecio(entrada.lower())


    def buscarProductoPorID(self, id_producto):
        return self.datos.buscarProductoPorID(id_producto)

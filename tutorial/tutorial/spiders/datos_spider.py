#from .CapaNegocios import Articulo
#from .Entidades import Usuario, Destacados, Categoria, Articulo
import scrapy
from scrapy.loader import ItemLoader
from ..items import Articulo
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from subprocess import call, run, Popen



class StarComputacionSpider(Spider):
    name = "StarComputacion"
    start_urls = ['http://www.starcomputacion.com.ar/monitores-23/']
    #start_urls = ['http://www.starcomputacion.com.ar/monitores-23/', 'http://www.starcomputacion.com.ar/teclados-45/',
    #              'http://www.starcomputacion.com.ar/discos-rigidos-67/']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('//div[@class="padder"]/ul/li')

        #ITERAR SOBRE TODOS LOS ARTICULOS
        for i, art in enumerate(articulos):
            loader = ItemLoader(item=Articulo(), selector=art)

            loader.add_xpath('nombre', './/div/h3/a/text()')
            loader.add_xpath('precio', './/div/a/text()')

            cat = response.url.split("/")[-2]
            finalUrl = loader.get_xpath('.//a/@href')
            fullUrl = 'http://www.starcomputacion.com.ar/' + finalUrl[0]

            loader.add_value('url', fullUrl)

            if cat == "teclados-45":
                loader.add_value('categoria', 'Teclados')
            elif cat == "monitores-23":
                loader.add_value('categoria', 'Monitores')
            elif cat == "discos-rigidos-67":
                loader.add_value('categoria', 'Almacenamiento')
            elif cat == "impresoras-24":
                loader.add_value('categoria', 'Impresoras')
            elif cat == "mouses-y-pads-41":
                loader.add_value('categoria', 'Mouse Y Pads')
            elif cat == "parlantes-42":
                loader.add_value('categoria', 'Parlantes')
            elif cat == "teclados-45":
                loader.add_value('categoria', 'Teclados')
            elif cat == "webcams-46":
                loader.add_value('categoria', 'Webcams')
            elif cat == "estabilizador-de-tension-39":
                loader.add_value('categoria', 'Estabilizadores')
            elif cat == "auriculares-gamers-141":
                loader.add_value('categoria', 'Auriculares')
            elif cat == "pendrives-13":
                loader.add_value('categoria', 'Pendrives')
            yield loader.load_item()#imprimir salida

class BigPointSpider(Spider):
    name = "BigPoint"
    start_urls = ['https://bigpoint.com.ar/procesadores/']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('//*[@id="main"]/ul/li')

        #ITERAR SOBRE TODOS LOS ARTICULOS
        for i, art in enumerate(articulos):
            loader = ItemLoader(item=Articulo(), selector=art)

            loader.add_xpath('nombre', './/div/div/div[1]/a/h2/text()')
            loader.add_xpath('precio', './/div/div/div[3]/div[1]/span/span/ins/span/text()')

            cat = response.url.split("/")[-2]
            loader.add_xpath('url', './/div/div/div[1]/a/@href')

            if cat == "procesadores":
                loader.add_value('categoria', 'Procesadores')
            elif cat == "motherboards":
                loader.add_value('categoria', 'Motherboards')
            elif cat == "memorias":
                loader.add_value('categoria', 'Memorias')
            elif cat == "almacenamiento":
                loader.add_value('categoria', 'Almacenamiento')
            elif cat == "impresoras":
                loader.add_value('categoria', 'Impresoras')
            elif cat == "placas-de-video":
                loader.add_value('categoria', 'Placas de Video')
            elif cat == "mouses-y-teclados":
                loader.add_value('categoria', 'Pack Mouses Y Teclados')
            elif cat == "fuentes":
                loader.add_value('categoria', 'Fuentes')
            elif cat == "gabinetes":
                loader.add_value('categoria', 'Gabinetes')
            elif cat == "monitores":
                loader.add_value('categoria', 'Monitores')
            elif cat == "webcams":
                loader.add_value('categoria', 'Webcams')
            elif cat == "auriculares":
                loader.add_value('categoria', 'Auriculares')
            elif cat == "parlantes-pc":
                loader.add_value('categoria', 'Parlantes')
            elif cat == "refrigeracion":
                loader.add_value('categoria', 'Refrigeración')
            yield loader.load_item()#imprimir salida


class ComerosSpider(Spider):
    name = "Comeros"
    start_urls = ['https://www.comeros.com.ar/categoria-producto/memorias/', 'https://www.comeros.com.ar/categoria-producto/partes-de-pc/computacion-gabinetes/']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('//*[@id="page-top"]/div[5]/div/div/div/div/div/div/div[2]/div[2]/li')

        #ITERAR SOBRE TODOS LOS ARTICULOS
        for i, art in enumerate(articulos):
            loader = ItemLoader(item=Articulo(), selector=art)

            #nom = loader.get_xpath('.//div/div[3]/h3/text()')[0].strip()
            #if nom != "Listado de sucursales OCA para retiro del producto":

            loader.add_xpath('nombre', './/div/div[3]/h3/text()')
            loader.add_xpath('precio', './/div/div[2]/p/span/text()')

            cat = response.url.split("/")[-2]
            loader.add_xpath('url', './/div/div[4]/a/@href')

            if cat == "computacion-microprocesadores":
                loader.add_value('categoria', 'Procesadores')
            elif cat == "computacion-motherboards":
                loader.add_value('categoria', 'Motherboards')
            elif cat == "memorias":
                loader.add_value('categoria', 'Memorias')
            elif cat == "discos-rigidos":
                loader.add_value('categoria', 'Almacenamiento')
            elif cat == "impresoras":
                loader.add_value('categoria', 'Impresoras')
            elif cat == "placas-de-video":
                loader.add_value('categoria', 'Placas de Video')
            elif cat == "ups":
                loader.add_value('categoria', 'UPSs')
            elif cat == "computacion-fuentes-de-alimentacion":
                loader.add_value('categoria', 'Fuentes')
            elif cat == "computacion-gabinetes":
                loader.add_value('categoria', 'Gabinetes')
            elif cat == "monitores":
                loader.add_value('categoria', 'Monitores')
            elif cat == "webcam":
                loader.add_value('categoria', 'Webcams')
            elif cat == "computacion-perifericos-auriculares":
                loader.add_value('categoria', 'Auriculares')
            elif cat == "computacion-perifericos-parlantes":
                loader.add_value('categoria', 'Parlantes')
            elif cat == "computacion-coolers":
                loader.add_value('categoria', 'Refrigeración')
            elif cat == "estabilizadores":
                loader.add_value('categoria', 'Estabilizadores')
            elif cat == "scanners":
                loader.add_value('categoria', 'Scanners')
            elif cat == "grabadoras":
                loader.add_value('categoria', 'Grabadoras')
            elif cat == "computacion-perifericos-joysticks":
                loader.add_value('categoria', 'Joysticks')
            elif cat == "computacion-perifericos-mouse":
                loader.add_value('categoria', 'Mouses')
            elif cat == "computacion-perifericos-teclados":
                loader.add_value('categoria', 'Teclados')
            yield loader.load_item()#imprimir salida

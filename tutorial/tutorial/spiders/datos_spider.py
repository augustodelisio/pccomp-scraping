#from .CapaNegocios import Articulo
#from .Entidades import Usuario, Destacados, Categoria, Articulo
import scrapy
from scrapy.loader import ItemLoader
from ..items import Articulo
from scrapy.spiders import Spider
from scrapy.selector import Selector
from string import capwords
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from subprocess import call, run, Popen



class StarComputacionSpider(Spider):
    name = "StarComputacion"
    start_urls = ['http://www.starcomputacion.com.ar/monitores-23/', 'http://www.starcomputacion.com.ar/teclados-45/',
                  'http://www.starcomputacion.com.ar/impresoras-24/', 'http://www.starcomputacion.com.ar/mouses-y-pads-41/',
                  'http://www.starcomputacion.com.ar/parlantes-42/', 'http://www.starcomputacion.com.ar/webcams-46/',
                  'http://www.starcomputacion.com.ar/estabilizador-de-tension-39/', 'http://www.starcomputacion.com.ar/pendrives-13/',
                  'http://www.starcomputacion.com.ar/auriculares-gamers-141/']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('//div[@class="padder"]/ul/li')

        #ITERAR SOBRE TODOS LOS ARTICULOS
        for i, art in enumerate(articulos):
            loader = ItemLoader(item=Articulo(), selector=art)

            loader.add_xpath('nombre', './/div/h3/a/text()')
            #loader.add_xpath('precio', './/div/a/text()')
            precio = loader.get_xpath('.//div/a/text()')[0]
            precio = precio.split('AR$')[-1].strip()
            loader.add_value('precio', precio)

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
    start_urls = ['https://bigpoint.com.ar/procesadores/', 'https://bigpoint.com.ar/motherboards/',
                  'https://bigpoint.com.ar/memorias/', 'https://bigpoint.com.ar/almacenamiento/',
                  'https://bigpoint.com.ar/impresoras/', 'https://bigpoint.com.ar/placas-de-video/',
                  'https://bigpoint.com.ar/mouses-y-teclados/', 'https://bigpoint.com.ar/fuentes/',
                  'https://bigpoint.com.ar/gabinetes/', 'https://bigpoint.com.ar/monitores/',
                  'https://bigpoint.com.ar/webcams/', 'https://bigpoint.com.ar/auriculares/',
                  'https://bigpoint.com.ar/parlantes-pc/', 'https://bigpoint.com.ar/refrigeracion/']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('//*[@id="main"]/ul/li')

        #ITERAR SOBRE TODOS LOS ARTICULOS
        for i, art in enumerate(articulos):
            loader = ItemLoader(item=Articulo(), selector=art)

            loader.add_xpath('nombre', './/div/div/div[1]/a/h2/text()')
            pre = loader.get_xpath('.//div/div/div[3]/div[1]/span/span/ins/span/text()')[0]
            pre = pre.split(',')
            precio = ""
            for i in pre:
                precio += str(i) + ""
            precio = precio[:-1]
            precio = precio.strip()
            loader.add_value('precio', precio)

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
    start_urls = ['https://www.comeros.com.ar/categoria-producto/memorias/',
                  'https://www.comeros.com.ar/categoria-producto/partes-de-pc/computacion-gabinetes/',
                  'https://www.comeros.com.ar/categoria-producto/partes-de-pc/placas-de-video/',
                  'https://www.comeros.com.ar/categoria-producto/perifericos/computacion-perifericos-auriculares/']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('//*[@id="page-top"]/div[5]/div/div/div/div/div/div/div[2]/div[2]/li')

        #ITERAR SOBRE TODOS LOS ARTICULOS
        for i, art in enumerate(articulos):
            loader = ItemLoader(item=Articulo(), selector=art)

            nom = loader.get_xpath('.//div/div[3]/h3/text()')[0].strip()
            if nom == "Listado de sucursales OCA para retiro del producto":
                break

            loader.add_value('nombre', nom)
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


class MarstechSpider(Spider):
    name = "Marstech"
    # start_urls = ['https://www.marstech.com.ar/listado/st=Perifericos;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=62;scat_id=3894;/GlobalBluePoint-ERP.aspx',
    # 'https://www.marstech.com.ar/listado/st=Perifericos;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=62;scat_id=3892;/GlobalBluePoint-ERP.aspx']

    start_urls = ['https://www.marstech.com.ar/listado/st=Perifericos;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=62;scat_id=3894;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Almacenamiento;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=51;scat_id=3863;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Almacenamiento;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=51;scat_id=3864;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Parlantes;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=62;scat_id=3897;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Mouse;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=62;scat_id=3893;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Perifericos;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=62;scat_id=3892;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Perifericos;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=62;scat_id=3895;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Almacenamiento;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=51;scat_id=3865;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Monitores%20y%20Proyectores;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=60;scat_id=3917;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Perifericos;g=0;b=1;or=5;c=3;e=6;h=1;m=172,199,293,179,180,173,209,235,277,178;A_PAGENUMBER=1;cat_id=62;scat_id=3894;/GlobalBluePoint-ERP.aspx',
    'https://www.marstech.com.ar/listado/st=Estabilizadores%20Y%20Ups;g=0;b=1;or=5;c=3;e=6;h=1;m=0;A_PAGENUMBER=1;cat_id=46;scat_id=3832;/GlobalBluePoint-ERP.aspx']

    def parse(self, response):
        sel = Selector(response)
        articulos = sel.xpath('//*[@id="divBody"]/div[3]/div/div[3]/div[2]/div/div')
        #//*[@id="divBody"]/div[3]/div/div[3]/div[2]/div
        #ITERAR SOBRE TODOS LOS ARTICULOS
        for i, art in enumerate(articulos):
            loader = ItemLoader(item=Articulo(), selector=art)

            loader.add_xpath('nombre', './/div/div/div/article/div/a/div[2]/p/text()')
            precio = loader.get_xpath('.//div/div/div/article/div/a/div[2]/h5/text()')[0]
            precio = precio.split('ARS')[-1].strip()
            loader.add_value('precio', precio)

            cat = response.url.split('/')[-2].split(';')[-2].split('scat_id=')[1]#devuelve num de categoria

            loader.add_xpath('url', './/div/div/div/article/div/a/@href')

            if cat == "3865":
                loader.add_value('categoria', 'Almacenamiento')
            elif cat == "3864":
                loader.add_value('categoria', 'Almacenamiento')
            elif cat == "3863":
                loader.add_value('categoria', 'Pendrives')
            elif cat == "3917":
                loader.add_value('categoria', 'Monitores')
            elif cat == "3893":
                loader.add_value('categoria', 'Mouses')
            elif cat == "3897":
                loader.add_value('categoria', 'Parlantes')
            elif cat == "3892":
                loader.add_value('categoria', 'Teclados')
            elif cat == "3895":
                loader.add_value('categoria', 'Webcams')
            elif cat == "3832":
                loader.add_value('categoria', 'Estabilizadores')
            elif cat == "3894":
                loader.add_value('categoria', 'Auriculares')
            elif cat == "3896":
                loader.add_value('categoria', 'Joysticks')
            yield loader.load_item()#imprimir salida



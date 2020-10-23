from multiprocessing import Pool
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from time import perf_counter


def ejecutaSpider(sp):
    process = CrawlerProcess(get_project_settings())
    process.crawl(sp)
    process.start()

# the script will block here until the crawling is finished

if __name__ == "__main__":
    t1 = perf_counter()
    p = Pool(4)
    p.map(ejecutaSpider, ['StarComputacion', 'BigPoint', 'Comeros', 'Marstech'])
    p.close()
    p.join()
    print("Tiempo CON multiprocesamiento", perf_counter() - t1)
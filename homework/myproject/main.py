import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1579068791.A.10F.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1579068823.A.074.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler', start_urls=target_urls, filename='test.json')
    process.start()

if __name__ == '__main__':
    main()

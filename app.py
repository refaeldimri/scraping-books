import requests
import logging
from pages.all_books_page import AllBooksPage
from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H%:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list...')

pageContent = requests.get('http://books.toscrape.com/').content
page = AllBooksPage(pageContent)

books = page.books

# for webPage in range(1, page.page_count):
#     url = 'https://books.toscrape.com/catalogue/page-' + str(webPage + 1) + '.html'
#     # url = f'https://books.toscrape.com/catalogue/page-{webPage + 1}.html'
#     pageContent = requests.get(url).content
#     page = AllBooksPage(pageContent)
#     books.extend(page.books)





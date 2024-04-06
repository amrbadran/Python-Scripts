import requests
from bs4 import BeautifulSoup
from FileHandler import *


class WebScrapper:
    url = "https://www.aljazeera.com/"

    def __init__(self, tag, path):
        self.tag = tag
        self.path = path
        self.url = self.url + tag
        self.page = None
        self.html_parser = None

    def scrape(self):
        self.page = requests.get(self.url)
        self.__set_html_parser(self.page.text)
        news = self.__news_to_list(self.html_parser.findAll("a", attrs={"class": "u-clickable-card__link"}))
        FileHandler(self.path, news).write()

    def __news_to_list(self, news):
        res = []
        for new in news:
            res.append(new.text)
        return res

    def __set_html_parser(self, page):
        self.html_parser = BeautifulSoup(page, "html.parser")



from bs4 import BeautifulSoup
import urllib3
import htmlParser
import yaml
import sys

class Scraper():
    def __init__(self):
        pass

    @staticmethod
    def create_soup(url):
        '''
        Creates and returns a "soup" with html content
        to be parsed
        '''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        http = urllib3.PoolManager()
        request = http.request('GET', url)
        data = request.data

        soup = BeautifulSoup(data, features="lxml")

        return soup
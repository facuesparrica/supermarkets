from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

wdriver = webdriver.Chrome('/Users/facu/PycharmProjects/Supermarkets/chromedriver')

wdriver.get('https://www.disco.com.ar/Login/PreHome.aspx')
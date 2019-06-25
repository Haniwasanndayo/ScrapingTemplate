import urllib.request

from bs4 import BeautifulSoup

from selenium import webdriver


# PhantomJSのドライバーを得る

browser = webdriver.PhantomJS()
browser.implicitly_wait(2)


# Loginアクセス＆スープ

url_login="hogehoge.com"

browser.get(url_login)

soup=bs4.BeautifulSoup(urllib.request.urlopen(url_login.read(), "html.parser")

#!/usr/bin/env python
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('~/Downloads/firefox/firefox')
#firefox_binary=binary)#executable_path='/usr/local/bbn/geckodriver')
browser = webdriver.Chrome("/home/maxd13/Downloads/chromedriver")
browser.get("http://127.0.0.1:8000")

assert 'Django' in browser.title

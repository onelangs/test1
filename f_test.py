# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 01:00:40 2016

@author: huang
"""

from selenium import webdriver
brower = webdriver.Firefox()
brower.get('http://localhost:8000')
assert 'To-Do' in brower.title

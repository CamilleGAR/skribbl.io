# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:44:23 2020

@author: camil
"""
from selenium import webdriver

class Canvas :
    def __init__(self, driver):
        self.zone_dessin = driver.find_element_by_xpath('//*[@id="canvasGame"]')
        self.mot = driver.find_element_by_xpath('//*[@id="currentWord"]')
        
    
        

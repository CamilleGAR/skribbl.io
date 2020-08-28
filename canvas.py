# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:44:23 2020

@author: camil
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib.colors as colors
import mouse
import time
from scipy.spatial import distance

def hex_to_rgb(hex_string):
    rgb = colors.hex2color(hex_string)
    return tuple([int(255*x) for x in rgb])


class Canvas :
    def __init__(self, driver):
        self.driver = driver
        self.zone_dessin = driver.find_element_by_xpath('//*[@id="canvasGame"]')
        self.mot = driver.find_element_by_xpath('//*[@id="currentWord"]')
        self.colors = self.get_colors()
        self.elements = self.get_elements()
        self.current_color = None
        self.crayons = {3 : driver.find_element_by_xpath('//*[@id="containerBoard"]/div[2]/div[4]/div[1]'),
                        7 : driver.find_element_by_xpath('//*[@id="containerBoard"]/div[2]/div[4]/div[2]'),
                        19 : driver.find_element_by_xpath('//*[@id="containerBoard"]/div[2]/div[4]/div[3]'),
                        40 : driver.find_element_by_xpath('//*[@id="containerBoard"]/div[2]/div[4]/div[4]')}
        
      
    def get_colors(self) :
        """Recupere toutes les couleurs disponibles"""
        
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.findAll('div', {'class' : 'colorItem'})
        
        id_color = 0
        colors_dict = dict()
        for div in divs :
            colors_dict[id_color] = self.color_convert(div['style'])
            id_color += 1
            
        return colors_dict
        
        
    def get_elements(self) :
        """Recupere toutes les cases couleurs à partir du xpath"""
        
        id_color = 0
        elements_dict = dict()
        
        for i in range(1,12) :
            elements_dict[id_color] = self.driver.find_element_by_xpath('//*[@id="containerBoard"]/div[2]/div[2]/div[1]/div[{}]'.format(i))
            id_color += 1
            
        for i in range(1,12) :
            elements_dict[id_color] = self.driver.find_element_by_xpath('//*[@id="containerBoard"]/div[2]/div[2]/div[2]/div[{}]'.format(i))
            id_color += 1
            
        return elements_dict
    

    def color_convert(self, style) :
        """transforme div['style'] = background: #xxxxxx -> rgb"""
        
        for i, char in enumerate(style) :
            if char == '#' : indice = i
            
        try :
            hexadecimal = style[indice:]
        except NameError :
            print('n\'est pas une couleur')
            
        if hexadecimal == '#FFF' :
            hexadecimal = '#FFFFFF'
        elif hexadecimal == '#000' :
            hexadecimal = '#000000'
        
        return hex_to_rgb(hexadecimal)
    
    def select_color(self, rgb) :
        """Renvoie la couleur de self.colors la plus proche"""
        
        colors_dict = dict()
        
        for k in self.colors.keys() :
            colors_dict[k] = distance.euclidean(rgb, self.colors[k])
            
        return min(colors_dict, key = lambda k : colors_dict[k])
            
    
    def draw(self, img_array, crayon_size) :
        """Dessine pixel par pixel sur le canvas"""
        
        x_start, y_start = self.zone_dessin.location.values()
        x_size, y_size = self.zone_dessin.size.values()
        
        self.crayons[crayon_size].click()           
        
        for i in self.elements :
            self.elements[i].click()
            
            y_clic = y_start +45
            for y in range(len(img_array)) :
                x_clic = x_start
                for x in range(len(img_array[0])) :
                    if i == self.select_color(img_array[y,x]) :
                        mouse.move(x_clic, y_clic)
                        time.sleep(0.0001)
                        mouse.click()
                        time.sleep(0.0001)
                    x_clic += crayon_size
                y_clic += crayon_size
        
        
        
 
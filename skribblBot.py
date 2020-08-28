# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:02:45 2020

@author: camil
"""

from selenium import webdriver
from tkinter import *
import keyboard
from imageFinder import ImageFinder
from imageTransformer import ImageTransformer
from skribblFormatConverter import SkribblFormatConverter
from parametrage import Parametrage
from canvas import Canvas

import time


class SkribblBot :
    
    """Dessine une image provenant de google image quand on appuie sur un bouton 'help'"""
    
    def __init__(self) :
        self.driver = webdriver.Chrome('chromedriver')
        self.img_finder = ImageFinder()
        self.img_transformer = ImageTransformer()
        #self.skribbl_converter = SkribblFormatConverter()
        self.parametrage = Parametrage(Tk(), self)
        self.parametrage.mainloop()
        
        
    def draw(self) :
        """Lance de dessin automatique"""
        
        self.canvas = Canvas(self.driver)
        
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.fullscreen_window()
        
        mot = self.canvas.mot.text
        x_canvas, y_canvas = self.canvas.zone_dessin.location.values()
        h_canvas, l_canvas = self.canvas.zone_dessin.size.values()
        taille_points = self.parametrage.crayon.get()
        
        img = self.img_finder(mot)
        
        self.img_transformer.set_dimensions(l_canvas, h_canvas)
        self.img_transformer.set_taille_points(int(taille_points))
        im_array = self.img_transformer(img)
        
        self.canvas.draw(im_array, int(taille_points))
        




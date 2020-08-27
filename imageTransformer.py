# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 22:09:05 2020

@author: camil
"""

from math import *
import numpy as np

class ImageTransformer :
    
    """
    Transforme les images (objets provenant de PIL) en array.
    """
    
    def __init__(self) :
        self.taille_points = 1
        
    def set_dimensions(self, dim_x, dim_y) :
        self.dim_x = dim_x
        self.dim_y = dim_y
        
    def set_taille_points(self, taille_points) :
        self.taille_points = taille_points
        
    def transform(self, image) :
        resized_dim_x = ceil(self.dim_x/self.taille_points)
        resized_dim_y = ceil(self.dim_y/self.taille_points)
        resized_image = image.resize((resized_dim_x, resized_dim_y))
        return np.array(resized_image)
        
    def __call__(self, image) :
        return self.transform(image)
    
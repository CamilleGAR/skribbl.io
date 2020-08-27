# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:24:09 2020

@author: camil
"""
from scipy.spatial import distance

class SkribblFormatConverter :
    
    """Transforme une image au format array en un format facilement utilisable
    sur skribbl.io"""
    
    def __init__(self, **colors) :
        self.colors = colors
        
    def color_converter(self, color) :
        """Renvoie la couleur de self.colors la plus proche"""
        
        colors_dict = dict()
        
        for k in self.colors.keys() :
            colors_dict[k] = distance.euclidean(color, self.colors[k])
            
        return min(colors_dict, key = lambda k : colors_dict[k])
        
        
    def image_converter(self, image, dim_x, dim_y) :
        """Convertit l'image format array -> dict {(x,y) : color}
        Color est une str"""
        
        nb_pixels_x = len(image[0])
        nb_pixels_y = len(image)
        
        pixels_colors = dict()
        for x in range(nb_pixels_x) :
            for y in range(nb_pixels_y) :
                pixels_colors[(x, y)] = self.color_converter(image[y,x])
                
        return pixels_colors
    
    def __call__(self, image, dim_x, dim_y) :
        return self.image_converter(image, dim_x, dim_y)
    
                
        
    
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:57:00 2020

@author: camil
"""

from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup

class ImageFinder :
    
    """
    Trouve une image sur internet à partir d'un mot.
    """
    
    
    def __init__(self) :
        pass
    
    
    def get_url(self, mot) :
        """Renvoie l'url google image en rapport avec le mot recherche"""
        
        url = \
'https://www.google.com/search?\
q={mot}\
&tbm=isch&ved=2ahUKEwifiaiG0bbrAhVHwYUKHZNLD50Q2-cCegQIABAA\
&oq={mot}\
&gs_lcp=CgNpbWcQA1AAWABgvlZoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZw&sclient=img&ei=QSlFX9_kN8eClwSTl73oCQ&bih=12&biw=25&hl=FR'\
.format(mot=mot)

        return url
    
    
    def get_html(self, url) :
        """Renvoie la page html correspondant à l'url"""
        
        return requests.get(url)
    
    
    def get_src(self, html) :
        """Renvoie l'adresse de la premiere image de la page html"""
        
        soup = BeautifulSoup(html.content, 'html.parser')
        img_class = soup.find_all('img')[1] #2nd element : 1st image on google
        src = img_class['src']
        
        return src
    
    
    def get_image(self, src) :
        """Renvoie l'image indiquée dans l'adresse src"""
        
        return Image.open(BytesIO(src.content))
        
    
    def image_from_word(self, mot) :
        """Renvoie un array representant une image du mot demandé
        Peut être appelé sans parametre si l'objet a été initialisé avec un mot"""
        
        url = self.get_url(mot)
        html = self.get_html(url)
        src = self.get_src(html)
        html_img = self.get_html(src)
        image = self.get_image(html_img)
        
        return image
            

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:39:46 2020

@author: camil
"""

from tkinter import *

class Parametrage(Frame):
    
    """Fenetre de parametrage du dessin"""
    
    def __init__(self, fenetre, skribbl, **kwargs):
        Frame.__init__(self, fenetre, width=100, height=100, **kwargs)
        self.pack(fill=BOTH)
        
        self.skribbl = skribbl
        
        # Création de nos widgets        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="right")
        
        self.bouton_cliquer = Button(self, text="help", fg="red", command=self.skribbl.draw)
        self.bouton_cliquer.pack(side="top")
    
        self.crayon = StringVar(value = 1)
        self.petit_crayon = Radiobutton(self, text="petit", variable=self.crayon, value="1")
        self.moyen_crayon = Radiobutton(self, text="moyen", variable=self.crayon, value="2")
        self.grand_crayon = Radiobutton(self, text="grand", variable=self.crayon, value="3")
        self.tres_grand_crayon = Radiobutton(self, text="tres grand", variable=self.crayon, value="4")
        self.petit_crayon.pack()
        self.moyen_crayon.pack()
        self.grand_crayon.pack()
        self.tres_grand_crayon.pack()
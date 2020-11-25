#!/usr/bin/env python
# coding: utf-8

# In[37]:


import tkinter as tk
import cv2 as c
from tkinter import ttk

root = tk.Tk()
root.title("Image Convertor")
root.resizable(False , False)

class File_convertor():
    def __init__(self):
        pass
    
    def layout(self):
        self.heading  =tk.Label(root , text  ="Image_Convertor" ,font = ("cursive" , 30))
        self.heading.grid(row = 0 , column=0)
        self.entry_name = tk.Entry(root , width = 20 , font  =("cursive" , 20))
        self.entry_name.grid(row = 1 , column = 0)
        self.drop_down = ttk.Combobox(root , width  =20 , font = (15))
        self.drop_down['values'] = ("jpg","png","jpeg","tiff","bmp","pgm")
        self.drop_down.grid(row = 2 , column=0,pady  =10)
        self.convert = tk.Button(root , text = "Convert" ,bg = "yellow")
        self.convert.grid(row  =3 , column=0)
        self.progress = tk.Label(root , text = "  ")
        self.progress.grid(row  =4 , column=0)
        
    def conversion(self):
        
        def get():
            self.entry_box = self.entry_name.get()
            self.drop = self.drop_down.get()
            point = '.'
            for a in self.entry_box:
                if point==a:
                    indx = self.entry_box.index(point)
            self.data = self.entry_box[:indx+1]
            
        def loop():
            try:
                image = c.imread(self.entry_box)
                name = self.data+self.drop
                c.imwrite(name,image)
                self.progress.config(text = f'Image Coverted\nSearch it as {self.data+self.drop}')
            except:
                self.progress.config(text = "Wrong Image Name\n Check the name you have written")
                
        def all():
            get()
            loop()
        self.convert.config(command  =all)
        
convertor = File_convertor()
convertor.layout()
convertor.conversion()
root.mainloop()


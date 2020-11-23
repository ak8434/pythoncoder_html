#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
from pytube import YouTube

root = tk.Tk()
root.title("Youtube Downloader")
root.resizable(False,False)

class Youtube():
    def __init__(self):
        pass
    
    def layout(self):
        self.enter = tk.Label(root , text ="Enter the url", font = ("cursive",30))
        self.enter.grid(row=0,column=0)
        self.entry_box = tk.Entry(root,width =60)
        self.entry_box.grid(row=1 , column=0)
        self.download_button = ttk.Button(root , text="Download")
        self.download_button.grid(row=2,column=0,sticky = 'e')
        self.label = tk.Label(root , text = " ")
        self.label.grid(row= 2 , column = 0)
         
        
    def pytube(self):
        
        def get():
            self.link = self.entry_box.get()
            
        def links():
            try: 
                url = self.link
                linker = YouTube(url)
                self.stream = linker.streams.first()
                self.label.config(text = "Download Started , Leave the gui as it is ")
            except:
                self.label.config(text = "Enter correct url")
        def bind():
            get()
            links()
            self.stream.download()
            
        self.download_button.config(command=bind)
                  
youtube = Youtube()
youtube.layout()
youtube.pytube()
root.mainloop()


import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import Menu

root =tk.Tk()
root.title("Webpage Extracter")
root.resizable(False , False)

class Layout():
    
    def frames(self):
        self.frame1 = tk.Frame(root)
        self.frame2 = tk.Frame(root)
        self.frame3 = tk.Frame(root)
        self.frame4 = tk.Frame(root)
        
    def menus(self):
        self.menu_bar = Menu(root)
        root.config(menu = self.menu_bar)
        def show():
            messagebox.showinfo("Aryan kumar", 'I am aryan kumar\n I wrote this app with motive to make web scraping easy.\n Thank You ')
        
        self.menu_ = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label = "About" , command = show)
        
    def heading(self):
        self.heading = tk.Label(self.frame1 , text = "Web Scraper" , font = ("Cursive",30))
        
    def combobox(self):
        self.combobox = ttk.Combobox(self.frame2 , width = 7) #for http:// or https://
        self.combobox['values'] = ("https://" ,"http://")
        self.combobox.current(0)
        
        self.combowww = ttk.Combobox(self.frame2 , width = 7) #for www.
        self.combowww['values'] = ("www.")
        self.combowww.current(0)
        
    def entry_box(self):
        self.entry = tk.Entry(self.frame2 , width = 20 ,font  =("cursive" ,12))
        
    def button(self):
        self.check = tk.Button(self.frame2 , text  ="Scrape" ,width  =12 ,bg = "green" ,fg = "white")
        
        
    def scrolltext(self):
        self.scrolledtext = scrolledtext.ScrolledText(self.frame3 , width = 100 , height =25)
        
    def labelframe(self):
        self.labelframe1  = tk.LabelFrame(self.frame4 ,text = "Title")
        self.labelframe2 = tk.LabelFrame(self.frame4 ,text = "Meta")
        self.labelframe3 = tk.LabelFrame(self.frame4 ,text = "Scipt")
        
    def label_frame_insert(self):
        self.scrolltxt = scrolledtext.ScrolledText(self.labelframe1 ,width = 40 ,height =3)
        self.scrolltxt1 = scrolledtext.ScrolledText(self.labelframe2 ,width =40 ,height =10)
        self.scrolltxt2 = scrolledtext.ScrolledText(self.labelframe3 ,width = 40 ,height = 10)
        
    def scraping(self):
        #adding functionality to the software
        
        def get():
            self.h1 = self.combobox.get()
            self.h2 = self.combowww.get()
            self.h3 = self.entry.get()
            self.h4 = self.h1+self.h2+self.h3
            
        def connect():
            self.get_web = requests.get(self.h4)
            self.get_text = self.get_web.text
            
        def beautify():
            self.soup = BeautifulSoup(self.get_text ,"html.parser")
            self.beauty = self.soup.prettify()
            
        def title():
            self.get_title =self.soup.title.string
            
        def page_meta():
            self.get_meta =self.soup.find_all("meta")
            
        def page_script():
            self.get_script  =self.soup.find_all("script")
            
        def insert_code():
            self.scrolledtext.insert(tk.INSERT ,self.beauty)
            self.scrolltxt.insert(tk.INSERT ,self.get_title)
            self.scrolltxt1.insert(tk.INSERT ,self.get_meta)
            self.scrolltxt2.insert(tk.INSERT ,self.get_script)
            
            
        def connect_all():
            get()
            connect()
            beautify()
            title()
            page_meta()
            page_script()
            insert_code()
            
        self.check.config(command = connect_all)
        
    def clear_save(self):
        self.clear = tk.Button(self.frame3 ,text = "Clear" ,width = 10 ,bg = "red" ,fg = "white")
        self.save = tk.Button(self.frame3 ,text = "Save" , width = 10 ,bg ="green" ,fg = "white")
        
    def save_clear_save(self):
        
        def clear():
            self.scrolledtext.delete("1.0","end")
            self.scrolltxt.delete("1.0","end")
            self.scrolltxt1.delete("1.0","end")
            self.scrolltxt2.delete("1.0","end")
            
        def new_gui():
            self.win = tk.Tk()
            self.win.title("Save")
            self.win.resizable(False , False)
            
            self.entry = tk.Entry(self.win  ,width = 15)
            self.entry.pack(pady = 10 ,padx =10)
            self.save_button = tk.Button(self.win ,text ="Save" ,bg = "green" ,fg = "white")
            self.save_button.pack()
            self.label = tk.Label(self.win , text = "  ")
            self.label.pack()
            def save():
                self.get_name = self.entry.get()
                self.get_data = self.scrolledtext.get("1.0","end")
                extension = ".txt"
                file = open(self.get_name+extension , "w")
                file.write(self.get_data)
                file.close()
                self.label.config(text = self.get_name+extension)
                
            self.save_button.config(command = save)
                
            self.win.mainloop()
            
        self.clear.config(command = clear)
        self.save.config(command =new_gui)
        
        
    def gradding(self):
        self.frame1.grid(row = 0 ,column = 0)
        self.frame2.grid(row = 1 ,column = 0)
        self.frame3.grid(row = 2 ,column = 0)
        self.frame4.grid(row = 2 , column = 1 ,sticky = "n")
        self.heading.grid(row = 0 , column  =0 , pady = 10)
        self.combobox.grid(row = 0 , column = 0)
        self.combowww.grid(row  =0 ,column = 1)
        self.entry.grid(row = 0 ,column = 2)
        self.check.grid(row =1 ,column=2 , sticky = "e")
        self.scrolledtext.grid(row = 0 ,column = 0)
        self.labelframe1.grid(row =0 , column  =1 , sticky  ="w")
        self.labelframe2.grid(row =1 , column  =1 , sticky  ="w")
        self.labelframe3.grid(row =2 , column  =1 , sticky  ="w")
        self.scrolltxt.grid(row = 0 , column = 0)
        self.scrolltxt1.grid(row = 0 , column = 0)
        self.scrolltxt2.grid(row = 0 , column = 0)
        self.clear.grid(row = 1 ,column =0 ,sticky = "e" ,padx = 80)
        self.save.grid(row = 1 ,column = 0 ,sticky = "e")
        
    def loop(self):
        root.mainloop()

        
        
layout = Layout()
layout.frames()
layout.menus()
layout.heading()
layout.combobox()
layout.entry_box()
layout.button()
layout.scraping()
layout.scrolltext()
layout.labelframe()
layout.label_frame_insert()
layout.clear_save()
layout.save_clear_save()
layout.gradding()
layout.loop()
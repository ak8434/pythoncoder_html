#!/usr/bin/env python
# coding: utf-8

# In[123]:


import tkinter as tk
from tkinter import ttk
from tkinter import *
import socket as s
import datetime
from tkinter import scrolledtext

win = tk.Tk()

class chatbot_ai():
    def __init__(self ,name ,time , date):
        self.name = name
        self.time = time
        self.date = date
        
    def layout(self):
        win.title("Chat bot")
        win.resizable(False , False)
        frame = ttk.Frame(win)#adding frame
        frame.grid(row= 0 , column =0)
        output_field = scrolledtext.ScrolledText(frame , width=40)#to show the text
        output_field.grid(row = 0 , column = 0)
        entry = tk.Entry(frame , width = 50 ,bg ="gold")#to give the data to the bot
        entry.grid(row = 1 , sticky ="w")
        button = ttk.Button(frame , text = "Send" , width=6)#to push the data to the bot
        button.grid(row = 1,sticky ="e")
        self.text = output_field
        self.entry_box = entry
        self.push = button
    
    def date__time(self):
        date_time = datetime.datetime.now()
        date = date_time.strftime("%d"+":"+"%m"+":"+"%y")
        time = date_time.strftime("%H"+":"+"%M"+":"+"%S")
        self.date = date
        self.time = time
        
    def ip(self):
        user = s.gethostname() #getting the user
        get_ip = s.gethostbyname(user) #getting the ip of the user
        self.user_name =user 
        self.get_ip = get_ip
        
    def get(self):
        
        def get_box():
            self.entry_data = self.entry_box.get()
            
        def clear_box():
            self.entry_box.delete(0,"end")
        
        def user():
            self.text.insert(tk.INSERT ,"\n [USER : "+self.entry_data+"]")
        
        def logic():
            get_box()
            if self.entry_data=="hi":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+"hello")
            clear_box()
            
            if self.entry_data=="your name":
                user()
                self.text.insert(tk.INSERT ,"\n PIB")
            
            if self.entry_data=="fullform":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+"Programmed Intellectual Body")
            
            if self.entry_data=="dob":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+"09:11:2020")
            
            if self.entry_data=="time":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+self.time)
            
            if self.entry_data=="date":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+self.date)
            
            if self.entry_data=="ip":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+self.get_ip)
            
            if self.entry_data=="user":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+self.user_name)
                
                
            if self.entry_data=="how are you":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+"I am good , how are you?")
            
            elif self.entry_data=="i am good":
                user()
                self.text.insert(tk.INSERT ,"\n BOT : "+"Awesome I felt awesome when you feel good.Tell me something more about you")
            
            elif self.entry_data=="what do you wanna know":
                user()
                self.text.insert(tk.INSERT ,"\n BOT : "+"Any thing you will say i will listen ,if you are not getting what to say then let me say ,what's your name")
                
            elif self.entry_data=="aryan":
                user()
                self.text.insert(tk.INSERT,"\n BOT : "+"It's a good name "+self.entry_data)
            
            elif self.entry_data=="how you were made":
                user()
                self.text.insert(tk.INSERT,"\n BOT : "+"It was just a random project and aryan wrote me")
                
            elif self.entry_data=="in which langauge you were written":
                user()
                self.text.insert(tk.INSERT , "\n BOT : "+"It was written in python and for gui tkinter is used")
                
            elif self.entry_data=="what is python":
                user()
                self.text.insert(tk.INSERT ,"\n BOT : "+"It is a scripting langauge made by Guido Van Russum in 1995")
                
            elif self.entry_data=="what is a scripting language":
                user()
                self.text.insert(tk.INSERT , "\n BOT : It just like a programming language but it uses a intereprter to compile the code.")
                
            elif self.entry_data=="what is a programming langauge":
                user()
                self.text.insert(tk.INSERT , "\n BOT :  A programming langauge is a set of instruction to a computer to perform")
                
            elif self.entry_data=="how many type of programming langauges are there":
                user()
                self.text.insert(tk.INSERT , "\n BOT : There are two type of programming language \n1.Low level programming langauges \n2.High level programming langauages")
                
            elif self.entry_data=="what is a string":
                user()
                self.text.insert(tk.INSERT , "\n BOT : Any thing inside a single or \ndouble quotes is known as a string.")
        
        self.push.config(command = logic)
        
        
chatbot = chatbot_ai(1,1,1)
chatbot.layout()
chatbot.date__time()
chatbot.ip()
chatbot.get()
win.mainloop()


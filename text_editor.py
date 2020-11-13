#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import os
root = tk.Tk()
root.title("Text editor")
root.resizable(False , True)

class Text_editor():
    def __init__(self):
        pass
    
    def layout(self):
        self.frame = ttk.Frame(root)
        self.frame.grid(row = 0 , column =0)
        self.text_box = scrolledtext.ScrolledText(self.frame,width =50,height = 20)
        self.text_box.grid(row =0,column=0)
        
    def new_button(self):
        
        def new_window():
            self.text_box.delete("1.0","end")
            
        def save_option():
            window =tk.Tk()
            window.title("Save")
            window.resizable(False ,False)
            save = tk.Label(window ,text= "Enter the name of the file")
            save.grid(row=0,column=0)
            self.save_name =ttk.Entry(window)
            self.save_name.grid(row=1,column=0)
            
            def get_save():#to get the name of the file to save
                self.data =self.save_name.get()
                self.file_data =self.text_box.get("1.0",tk.END)
                f =open(self.data+".txt","w")
                f.write(self.file_data)
                f.close()
                window.destroy()
            save_buton =ttk.Button(window,text ="Save",command =get_save)
            save_buton.grid(row=2,column=0)
            
            
        self.save =ttk.Button(self.frame,text="Save",command =save_option)
        self.save.grid(row=1,column=0,sticky="e")
        self.new =ttk.Button(self.frame,text ="New",command =new_window)
        self.new.grid(row =1 , column=0)
        

        
text_editor =Text_editor()
text_editor.layout()
text_editor.new_button()
root.mainloop()


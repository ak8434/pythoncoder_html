#txt editor
import tkinter as tk
from os import path
from tkinter import filedialog as fd
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import ttk

root = tk.Tk()
root.title("Text Editor")

class TextEditor():
    
    def frames(self):
        #ading frames
        self.frame = tk.Frame(root)
        self.frame0 = tk.Frame(root)
        
    def menu_bar(self):
        #creating menubars
        self.menu_get  = Menu(root)
        root.config(menu = self.menu_get)
        
    def new(self):
        
        def create_box():
            win = tk.Tk()
            win.title("Create File")
            win.resizable(False , False)
            label = tk.Label(win , text = "New file")
            label.pack(padx = 10 ,pady = 10)
            self.entry = tk.Entry(win)
            self.entry.pack(padx = 10 ,pady = 10)
            self.options = ttk.Combobox(win , width = 8)
            self.options["values"] = ("py","txt","html")
            self.options.pack(padx = 5)
            self.button = tk.Button(win ,text = "Create file")
            self.button.pack(padx = 10 ,pady  =10)
            self.create_label = tk.Label(win , text = " " )
            self.create_label.pack()
            
            def extract_name():
                self.get_text = self.entry.get()
                self.get_text_option = self.options.get()
                dot = "."
                self.full_name =self.get_text+dot+self.get_text_option
                print(self.full_name)
                
            def creating_file():
                self.create = open(self.full_name ,"w")
                self.create_open = self.create.write("  ")
                self.create.close()
                
            def opening_create_file():
                self.txtarea.delete(1.0 ,"end")
                self.read_file = open(self.full_name ,"r")
                self.insert_text = self.read_file.read()
                self.read_file.close()
                self.txtarea.insert(tk.INSERT , self.insert_text)
                
            def connector():
                extract_name()
                creating_file()
                opening_create_file()
                 
            self.button.config(command = connector)
            
        self.file_menu = Menu(self.menu_get)
        self.file_menu.add_command(label = "New" , command = create_box)
        
    def open(self):
        
        def file_open(): # opening files
            self.default_path = path.dirname(__file__)
            self.ask_file = fd.askopenfilename(parent = root ,title = "open file",initialdir = self.default_path , filetypes = (("Text","*.txt") , ("Python","*.py") ,("HTML","*.html")))
            self.read = open(self.ask_file ,"r")
            self.get_text = self.read.read()
            self.read.close()
            self.txtarea.insert(tk.INSERT , self.get_text)
        self.file_menu.add_command(label = "Open" ,command = file_open)
        
    def save(self):
        
        def file_save():
            #get text
            try:
                get_text  =self.txtarea.get(1.0 ,"end")
                write_file = open(self.ask_file , "w")
                write_file.write(get_text)
                write_file.close()
                
            except:
                get_text  =self.txtarea.get(1.0 ,"end")
                write_file = open(self.full_name , "w")
                write_file.write(get_text)
                write_file.close()
        
        self.file_menu.add_command(label = "Save" , command = file_save)
        
    def file(self):
        #adding element in the menu bar
        self.menu_get.add_cascade(label = "File" , menu = self.file_menu)
        
    def save_as(self):
        
        def file_save_as(): # save as
            win = tk.Tk()
            win.title("Save as")
            win.resizable(False , False)
            self.enter = tk.Entry(win)
            self.enter.pack(padx =10 , pady = 10)
            self.combo = ttk.Combobox(win , width = 8)
            self.combo["values"] =("py","txt","html")
            self.combo.pack()
            self.button = tk.Button(win , text = "Save")
            self.button.pack(padx = 10 ,pady = 5)
            self.label = tk.Label(win , text  = "  ")
            self.label.pack()
            
            def get_and_save():
                dot = "."
                self.get_save = self.txtarea.get(1.0 ,"end")
                self.get_entry = self.enter.get()
                self.get_combo = self.combo.get()
                self.all_combine = self.get_entry+dot+self.get_combo
                file = open(self.all_combine ,"w")
                file.write(self.get_save)
                file.close()
                self.label.config(text = self.all_combine)
                
            self.button.config(command = get_and_save)
        
        self.file_menu.add_command(label = "Save As" , command = file_save_as)
        
    def exit_option(self):
        
        def exitall(): #exit option
            root.quit()
            root.destroy()
            
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit" , command = exitall)
        
    def about(self):
        self.file_about = Menu(self.menu_get)
        self.file_about.add_command(label = "About")
        self.menu_get.add_cascade(label = "About us" , menu = self.file_about)
        
    def get_zoom(self):
        self.file_zoom = Menu(self.menu_get)
        self.menu_get.add_cascade(label = "Zoom" , menu = self.file_zoom)
        
    def increase(self):
        
        def increase_size():
            self.txtarea.config(font = ("cursive",5) ,width = 334 , height = 92)
        
        def increase_size_0():
            self.txtarea.config(font = ("cursive",10) ,width = 192)
        
        def increase_size_1():
            self.txtarea.config(font = ("cursive",15))
            
        def increase_size_2():
            self.txtarea.config(font = ("cursive",35))
            
        def increase_size_3():
            self.txtarea.config(font = ("cursive",70))
        
        def increase_size_4():
            self.txtarea.config(font = ("cursive",85))
            
        def increase_size_5():
            self.txtarea.config(font = ("cursive",100))
            
        
        self.file_zoom.add_command(label = "5" , command = increase_size)
        self.file_zoom.add_command(label = "10" , command = increase_size_0)
        self.file_zoom.add_command(label = "15" , command = increase_size_1)
        self.file_zoom.add_command(label = "35" , command = increase_size_2)
        self.file_zoom.add_command(label = "70" , command = increase_size_3)
        self.file_zoom.add_command(label = "85" , command = increase_size_4)
        self.file_zoom.add_command(label = "100" , command = increase_size_5)
        
        
    def scrolledtext(self):
        
        self.txtarea = scrolledtext.ScrolledText(self.frame ,width = 168 ,height = 40)
        
    def themes(self):
        self.txt_theme = Menu(self.menu_get)
        self.menu_get.add_cascade(label = "Themes" , menu = self.txt_theme)
        
    def light(self):
        
        def light_theme(): #light theme
            self.txtarea.config(bg = "white" ,fg = "black")
            
        self.txt_theme.add_command(label = "Light" , command = light_theme)
        
    def dark(self):
        
        def dark_theme(): # dark theme
            self.txtarea.config(bg = "black" ,fg = "white")
            
        self.txt_theme.add_command(label = "Dark" , command = dark_theme)
        
    def gray(self):
        
        def gray_theme(): #gray theme
            self.txtarea.config(bg = "gray" ,fg = "white")
            
        self.txt_theme.add_command(label = "Gray" ,command = gray_theme)
        
        
    def clear_copy(self):
         #clearining all elements
        def clear_all():
            self.txtarea.delete(1.0,"end")
            
        self.clear = tk.Button(self.frame0 , text = "Clear" ,width = 15 ,bg = "red" ,fg = "white" , command = clear_all)
             
    def grid(self):
        #gridding
        self.frame.grid(row = 0 , column  =0)
        self.frame0.grid(row = 1 , column  =0 ,sticky= "e")
        self.txtarea.grid(row = 0 ,column  =0 , padx = 5 , pady = 5)
        self.clear.grid(row = 0 , column = 0 ,padx = 10)
               
texteditor = TextEditor()
texteditor.frames()
texteditor.scrolledtext()
texteditor.menu_bar()
texteditor.new()
texteditor.open()
texteditor.save()
texteditor.file()
texteditor.save_as()
texteditor.exit_option()
texteditor.about()
texteditor.get_zoom()
texteditor.increase()
texteditor.themes()
texteditor.light()
texteditor.dark()
texteditor.gray()
texteditor.clear_copy()
texteditor.grid()
root.mainloop()
from tkinter import ttk
import tkinter as tk 


class MAINAPP(tk.Tk):
    def __init__(self, title):
        super().__init__()

        self.title(title)
        self.geometry("750x600")
        self.minsize(750,600)
        
        self.menu = Side_menu(self)

        self.mainloop()

class Side_menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__()
        ttk.Label(self,background="#0A2647").pack(expand=True, fill="both")
        self.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        encrypt_btn = ttk.Button(self, text="ENCRYPT")
        
        

    def create_layout(self):
        self.columnconfigure((0,1),weight=1,uniform='a')
        self.rowconfigure((0,1,2,3,4),weight=1, uniform='a')
        
        encrypt_btn.grid(row=1,column=0, rowspan=2)
        

    
MAINAPP(title="app")
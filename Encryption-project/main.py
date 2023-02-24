import os
import tkinter as tk
from tkinter import TclError, ttk
import webbrowser
import windows


#main frame
class MAINAPP(tk.Tk):
    def __init__(self, title):
        super().__init__()
        # title, geometry for main window 
        self.title(title)
        self.geometry("750x600")
        self.resizable(False,False)

        # icon photo
        try:
            self.icon_pci = tk.PhotoImage("media/shield.png")
            self.iconphoto(False,self.icon_pci)
        except TclError:
            pass
        
        img_dark = tk.PhotoImage(file='media/bg_dark.png')
        img_ligth = tk.PhotoImage(file='media/bg_ligth.png')
        help_img = tk.PhotoImage(file="media/help_icon.png")
        images = [img_dark, img_ligth,help_img]
        bg_c = ["#000518","#FFFFFF","#18A664"]
        # call frame
        self.image_menu = image_menu(self,images, bg_c)
        #run main window
        self.mainloop()

 
# side lobby label
class Side_menu(ttk.Frame):
    def __init__(self,parent,bg_colour,dark_or_not,help_image):
        super().__init__(parent)

        ttk.Label(self,background=bg_colour).pack(expand=True, fill="both")

        self.place(relx=0.5, y=0, relwidth=0.5, relheight=1)

        self.create_widgets(dark_or_not,help_image)

        self.dark_or_not = dark_or_not

            

    # create widget for left side menu
    def create_widgets(self,dark_or_not,help_image):

        def encrpyt_btn_cmd():
            windows.en_window(dark_or_not)

        def decrypt_btn_cmd():
            windows.de_window(dark_or_not)

        # theme logic
        self.frg_clr = None
        self.bg_clr  = None 
        self.help_image = help_image

        if dark_or_not:
            self.frg_clr = "#A0ADA1"
            self.bg_clr =  "#000000"
        else:
            self.frg_clr = "#7069DA"
            self.bg_clr  = "#FFFFFF"
        # encrypt button
        encrypt_btn = tk.Button(self, text="ENCRYPT",
                                     fg=self.frg_clr,
                                     bg=self.bg_clr,
                                     borderwidth=0,
                                     highlightthickness=0,
                                     font=("Comic Sans MS", 20, "bold"),
                                     command=encrpyt_btn_cmd)
        encrypt_btn.place(relx=0.33, y=200, relwidth=0.40, height=60)
        # Decrpyt button 
        decrypt_btn = tk.Button(self, text="DECRYPT",
                                    fg=self.frg_clr,
                                    bg=self.bg_clr,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    font=("Comic Sans MS", 20, "bold"),
                                    command=decrypt_btn_cmd)
        decrypt_btn.place(relx=0.33, y=350, relwidth=0.40, height=60)

        #help button
        def help_btn_cmd():
            top = tk.Toplevel()
            top.geometry("300x300")
            top.resizable(False,False)
            top.title("help centre")
            help_label = tk.Label(top,background="#FFFFFF",
                                foreground="#000000",
                                font=("Adobe Caslon Pro", 10),
                                text="This is basic Encryption app\nTo encrypt/decrypt click on buttons\nand respectively proceed further\n\nOR\n\nyou can visit our site below\n")
            help_label.pack(expand=True, fill="both")

            def site_btn():
                url = "https://twinkle1gupta.github.io/twinkle1gupta.io/help.html"
                webbrowser.open_new_tab(url)

            site_btn = tk.Button(top,command=site_btn,font=("Adobe Caslon Pro", 10,"bold"),anchor="s",text="https://twinkle1gupta.io/",borderwidth=0,highlightbackground="#FFFFFF",highlightcolor="#FFFFFF",highlightthickness=0,foreground='#000000',background="#FFFFFF")
            site_btn.place(relx=0,rely=0.75,relwidth=1)

        #help_button
        # help_img = tk.PhotoImage(file="media/help_icon.png")
        help_btn = tk.Button(self,image=help_image,
                                borderwidth=0,
                                background=self.bg_clr,
                                highlightthickness=0,
                                command=help_btn_cmd)
        help_btn.place(x=320,y=550,height=30,width=30)

    

# side image label
class image_menu(ttk.Frame):
    def __init__(self,master,image, background_colour):
        super().__init__(master)

        # background
        self.bkc_clr = background_colour
        self.img_clr = image

        # dark n light mode logic
        self.dark = True 

        def cmd():

            if self.dark:

                btn.config(text="Dark Theme: On")

                btn.config(background= self.bkc_clr[0],
                            foreground          = self.bkc_clr[1],
                            highlightcolor      = "black",
                            highlightbackground = "black",)
                L.config(image=self.img_clr[0])
                Side_menu(self,"#000000",self.dark,self.img_clr[2])

                self.dark = False

            else:

                btn.config(text="Dark Theme: Off")

                btn.config(background= self.bkc_clr[1],
                            foreground          = self.bkc_clr[0],
                            highlightcolor      = "#FFFFFF",
                            highlightbackground = "#FFFFFF")
                L.config(image=self.img_clr[1])
                Side_menu(self,"#FFFFFF", self.dark,self.img_clr[2])
                
                self.dark = True

        # place label along with left side menu
        L = ttk.Label(self,image=self.img_clr[0], background=self.bkc_clr[0], borderwidth=0)
        L.pack(expand=True,fill="both")

        Side_menu(self,"#000000",self.dark,self.img_clr[2])
        self.place(x=0,y=0,height=600,width=750)
        # place theme button
        btn = tk.Button(self,text               = "Dark Theme: ON",
                            background          = "#000000", 
                            foreground          = "#FFFFFF",
                            highlightcolor      = "#000518",
                            highlightbackground = "#000518",
                            highlightthickness=1,
                            borderwidth=0,
                            command=cmd)
        btn.place(x=20,y=550)


MAINAPP(title="An Improved Crypto System")


import os
from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser


class CustomDialougeBoxToCopyText(Toplevel):
    def __init__(self,master,title=NONE,text=NONE):
        super().__init__
        Toplevel.__init__(self, master)
        self.master = master

        self.label = Label(self,text=f"THIS IS YOUR {title}",
                            background="#FFFFFF", 
                            borderwidth=0,
                            foreground="#000000",
                            highlightbackground="#FFFFFF",
                            highlightcolor="#FFFFFF",
                            highlightthickness=0)
        self.label.place(x=100,width=200,y=20)
        self.text_box = Text(self)
        self.text_box.place(x=0,y=60,width=400,height=280)
        self.text_box.insert("1.0",text)
        self.title(title)
        self.geometry("400x400")
        self.configure(background="#FFFFFF")
        self.text_box.config(state="disabled")


        button1 = Button(self, text="OK",
                                command=self.buttonpressed,
                                background="#C38FFF",
                                borderwidth=0,
                                foreground="#000000",
                                highlightbackground="#FFFFFF",
                                highlightcolor="#FFFFFF",
                                highlightthickness=0)
        button1.place(x=10,y=360,width=100)

        button2 = Button(self,text="copy_text",
                         command=lambda: self.copy_text(text),
                         background="#C38FFF",
                         borderwidth=0,
                         foreground="#000000",
                         highlightbackground="#FFFFFF",
                         highlightcolor="#FFFFFF",
                         highlightthickness=0)
        button2.place(x=290,y=360,width=100)

    def buttonpressed(self):
        self.master.destroy()

    def copy_text(self,data):
        self.clipboard_append(data)
        




def window(theme_of_app, tit_le):

    root = Tk()

    # geometry and title
    root.geometry("750x600-100-200")
    root.resizable(False,False)
    root.title(tit_le)

    # text box
    text_box_label = Label(root, bg="#121212",fg="#FFFFFF" ,text="Enter text below", anchor="n", font=("Adobe Caslon Pro", 10))
    text_box_label.place(x=10,y=10, width=500, height=300)

    text_box = Text(root,bg="grey",fg="#FFFFFF", font=("Adobe Caslon Pro", 10),borderwidth=0,highlightbackground="#121212",highlightcolor="#121212",highlightthickness=0)
    text_box.place(x=25,y=45, width=470, height=220)

    # error message box
    def show_error(description):
        messagebox.showerror("Error",description)
        root.destroy()

    #help button command
    def help_btn_cmd():
        top = Toplevel()
        top.geometry("300x300")
        top.resizable(False,False)
        top.title("help centre")
        help_label = Label(top,background="#FFFFFF",
                            foreground="#000000",
                            font=("Adobe Caslon Pro", 10),
                            text="This is basic Encryption app\n\nto use this app \nselect file \nand\n click on Encrypt/Decrypt file button\nto encrpyt or decrpyt\n\nor in Text box you can enter \ntext to encrypt/decrypt \nand save it in .txt fileOR\n\nyou can visit our side below")
        help_label.pack(expand=True, fill="both")
        def site_btn():
                url = "https://twinkle0gupta.github.io/"
                webbrowser.open_new_tab(url)

        site_btn = Button(top,command=site_btn,anchor="s",text="https://twinkle0gupta.github.io/",borderwidth=0,highlightbackground="#FFFFFF",highlightcolor="#FFFFFF",highlightthickness=0,foreground='#000000',background="#FFFFFF",font=("Adobe Caslon Pro", 10,"bold"))
        site_btn.pack(fill="both")

    #help_button
    help_img = PhotoImage(file="media/help_icon.png",master=root)
    help_btn = Button(root,image=help_img,
                            borderwidth=0,
                            background="#000000",
                            highlightbackground="#000000",
                            highlightcolor="#000000",
                            highlightthickness=0,
                            command=help_btn_cmd)
    help_btn.place(x=680,y=560,height=30,width=30)

    # import file box
    import_box_label = Label(root, bg="#121212")
    import_box_label.place(x=10, y= 355, width=500, height=190) 

    def open():
        global file
        
        file = filedialog.askopenfile(initialdir=os.getcwd(),mode='r',
                                title="select file",
                                filetypes=(("Text files", "*.txt"),("CSV files","*.csv"),("MarkDown files","*.md"),("All file types", "*.*")))
        if file:
            if theme:
                open.file_name_label = Label(root,text="The file selected is \n`"+str(os.path.split(file.name)[1])+"`\nfrom path\n"+str(file.name),
                                        font=("Adobe Caslon Pro", 10),bg="#121212",fg="#FFFFFF")
            else:
                open.file_name_label = Label(root,text="The file selected is \n`"+str(os.path.split(file.name)[1])+"`\nfrom path\n"+str(file.name),
                                        font=("Adobe Caslon Pro", 10),bg="#FFFFFF",fg="#000000")
            open.file_name_label.place(x=30,y=450, width=450, height=90)

    open_file_btn = Button(root, text="select file!", command=open, background          = "#C38FFF", 
                                                                    foreground          = "#000000",
                                                                    highlightcolor      = "#C1A2E5",
                                                                    highlightbackground = "#C1A2E5",
                                                                    highlightthickness=0,
                                                                    borderwidth=0,
                                                                    font=("Adobe Caslon Pro", 10))
    open_file_btn.place(x=125,y=380, width= 250, height=50)


    #encrypt
    def encrypt_frame():

        encrypt_frame.master_pas_enctry_label = Label(root,text="Enter master password\n(must be rembebered):",
                                            background="#121212",
                                            foreground="#FFFFFF",
                                            font=("Adobe Caslon Pro", 10))
        encrypt_frame.master_pas_enctry_label.place(x=540,y=60,width=180)


        encrypt_frame.master_pas_enctry = Text(root, background = "grey", 
                                    foreground          = "#FFFFFF",
                                    highlightcolor      = "#C1A2E5",
                                    highlightbackground = "#C1A2E5",
                                    highlightthickness=0,
                                    borderwidth=0,
                                    font=("Adobe Caslon Pro", 10))
        encrypt_frame.master_pas_enctry.place(x=560,y=120,relheight=0.1,relwidth=0.2)

        # function when text box entity is being encrypted
        def enc_btn_enc_frame():
            # from crypto custom import main_enc function which takes message and password to encrypt passwod and save it to .txt file
            from crypto import main_enc as save_enc_file
            try:
                if text_box.get("1.0",'end-1c') == "":
                    messagebox.showerror("Invalid entry","Entry filed is empty")
                else:
                    message  =  text_box.get("1.0",'end-1c')
            except:
                pass

            try:
                if encrypt_frame.master_pas_enctry.get("1.0",'end-1c') == "":
                    messagebox.showerror("Invalid entry","Password filed is empty")
                else:
                    password = encrypt_frame.master_pas_enctry.get("1.0",'end-1c')
                    file_name_en, encrypted_message_,salt = save_enc_file(password,message)
                    encrypted_message_ = encrypted_message_.decode("ASCII")
                    salt = salt.hex()
                    file_name_en_req = file_name_en.split("/")[-1]
                    
                    messagebox.showinfo("successful",f"Text encryption successful!\nYour encrypted file is saved to /Encrypted_files/{file_name_en_req}")
                    CustomDialougeBoxToCopyText(root,"Encrpyted text", f"{encrypted_message_}||{salt}")
            except:
                pass

        encrypt_frame.enc_btn = Button(root,text="Encrypt text", background = "#C38FFF", 
                                    foreground          = "#000000",
                                    highlightcolor      = "#C1A2E5",
                                    highlightbackground = "#C1A2E5",
                                    highlightthickness=0,
                                    borderwidth=0,
                                    font=("Adobe Caslon Pro", 10),
                                    command=enc_btn_enc_frame)
        encrypt_frame.enc_btn.place(x=560,y=250,relheight=0.1, relwidth=0.2)

        def enc_file():
            from crypto import FileEncrypter
            try:
                if encrypt_frame.master_pas_enctry.get("1.0",'end-1c') == "":
                    messagebox.showerror("Invalid entry","Password filed is empty")
                else:
                    password = encrypt_frame.master_pas_enctry.get("1.0",'end-1c')
                    FileName =  FileEncrypter(file.name,password).check_ext()
                    messagebox.showinfo("successful",f"File encryption successful!\nYour encrypted file is saved to /Encrypted_files/{FileName}")
            except:
                pass
    
        encrypt_frame.enc_file_btn = Button(root,text="Encrypt file", background = "#C38FFF", 
                                    foreground          = "#000000",
                                    highlightcolor      = "#C1A2E5",
                                    highlightbackground = "#C1A2E5",
                                    highlightthickness=0,
                                    borderwidth=0,
                                    font=("Adobe Caslon Pro", 10),
                                    command=enc_file)
        encrypt_frame.enc_file_btn.place(x=560,y=400,relheight=0.1, relwidth=0.2)
        
   
    #decrypt
    def decrypt_frame():

        decrypt_frame.master_pas_entry_label = Label(root,   text = "Enter master password\nto decrypt:",
                                                        background = "#121212",
                                                        foreground = "#FFFFFF",
                                                        font       = ("Adobe Caslon Pro", 10))
        decrypt_frame.master_pas_entry_label.place(x=540,y=60,width=180)


        decrypt_frame.master_pas_entry = Text(root, background = "grey", 
                                            foreground          = "#FFFFFF",
                                            highlightcolor      = "#C1A2E5",
                                            highlightbackground = "#C1A2E5",
                                            highlightthickness  = 0,
                                            borderwidth         = 0,
                                            font                = ("Adobe Caslon Pro", 10))
        decrypt_frame.master_pas_entry.place(x=560,y=120,relheight=0.1,relwidth=0.2)
    
        def dec_btn_dec_frame():

            from crypto import main_dec 
            try:
                if text_box.get("1.0","end-1c") == "":
                    messagebox.showerror("Invalid entry","Entry field is empty")
                else:
                    ecn_text = text_box.get("1.0",'end-1c')
            except:
                pass

            try:
                if decrypt_frame.master_pas_entry.get("1.0",'end-1c') == "":
                    messagebox.showerror("Invalid entry","Password field is empty")
                else:
                    passwrod = decrypt_frame.master_pas_entry.get("1.0",'end-1c')
                    try:
                        file_name_de,decrypt_message_ = main_dec(passwrod,ecn_text)
                        file_name_req = file_name_de.split("/")[-1]
                        
                        messagebox.showinfo("successful",f"Text encryption successful!\nYour encrypted file is saved to /Encrypted_files/{file_name_req}")
                        CustomDialougeBoxToCopyText(root, "Decrypted Text",decrypt_message_)
                    except:
                        messagebox.showwarning("Wrong password","YOU TYPED INVALID PASSWORD\nTRY AGAIN WITH RIGTH PASSWORD")
            except:
                pass



        decrypt_frame.dec_btn = Button(root,text="Decrypt text", background = "#C38FFF", 
                                    foreground          = "#000000",
                                    highlightcolor      = "#C1A2E5",
                                    highlightbackground = "#C1A2E5",
                                    highlightthickness=0,
                                    borderwidth=0,
                                    font=("Adobe Caslon Pro", 10),
                                    command=dec_btn_dec_frame)
        decrypt_frame.dec_btn.place(x=560,y=250,relheight=0.1, relwidth=0.2)

        def dec_file():
            from crypto import FileDecryptor
            try:
                if decrypt_frame.master_pas_entry.get("1.0",'end-1c') == "":
                    messagebox.showerror("Invalid entry","Password field is empty")
                else:
                    passwrod = decrypt_frame.master_pas_entry.get("1.0",'end-1c')
                    FileName = FileDecryptor(file.name,passwrod).check_ext()
                    messagebox.showinfo("successful",f"File decryption successful!\nYour decrypted file is saved to /Decrypted_files/{FileName}")
            except:
                pass

        decrypt_frame.dec_file_btn = Button(root,text="Decrypt file", background = "#C38FFF", 
                                    foreground          = "#000000",
                                    highlightcolor      = "#C1A2E5",
                                    highlightbackground = "#C1A2E5",
                                    highlightthickness=0,
                                    borderwidth=0,
                                    font=("Adobe Caslon Pro", 10),
                                    command=dec_file)
        decrypt_frame.dec_file_btn.place(x=560,y=400,relheight=0.1, relwidth=0.2)

    # line seperator
    sep = Label(root, bg="#121212",
                        text="or you can import file down below",
                        fg="#A0ADA1",
                        font=("Adobe Caslon Pro", 10))
    sep.place(x=10, y=320, width=500, height=25)
                                       
    # side panel box
    side_panel = Label(root, bg="#121212")
    side_panel.place(x=530, y=10, width=202, height=535)

    if tit_le == "Encrypt":
        encrypt_frame()
    elif tit_le == "Decrypt":
        decrypt_frame()
    else:
        show_error("An unexpected error occurred")

    try:
        icon_pci = PhotoImage("media/shield.png")
        root.iconphoto(False,icon_pci)
    except TclError:
        pass

    global theme
    theme = theme_of_app

    # theme logic
    def cmd(theme):
        if theme:
            btn.config(text="Dark Theme: On")
            btn.config(background           = "#000000",
                        foreground          = "#FFFFFF",
                        highlightcolor      = "black",
                        highlightbackground = "black",
                        command=lambda: cmd(theme))

            root.config(background="#000000")

            text_box_label.config(background="#121212",fg="#FFFFFF",)
            sep.config(background="#121212", fg="#A0ADA1")
            import_box_label.config(background="#121212")
            side_panel.config(background="#121212")
            help_btn.config(background="#000000",highlightbackground="#000000",highlightcolor="#000000",highlightthickness=0)
            text_box.config(bg="grey",fg="#FFFFFF",highlightbackground="#121212",highlightcolor="#121212",highlightthickness=0)
            if tit_le == "Encrypt":
                encrypt_frame.master_pas_enctry_label.config(background="#121212",foreground="#FFFFFF")
                encrypt_frame.master_pas_enctry.config(foreground="#FFFFFF")
            else:
                pass
            if tit_le == "Decrypt":
                decrypt_frame.master_pas_entry.config(foreground="#FFFFFF")
                decrypt_frame.master_pas_entry_label.config(background="#121212",foreground="#FFFFFF")
            else:
                pass
            try:
                open.file_name_label.config(background="#121212",foreground="#FFFFFF")
                
            except AttributeError:
                pass

            theme = False
        else:
            btn.config(text="Dark Theme: Off")
            btn.config(background           = "#85B1CD",
                        foreground          = "#000000",
                        highlightcolor      = "#85B1CD",
                        highlightbackground = "#85B1CD",
                        command = lambda: cmd(theme))
            root.config(background="#85B1CD")
            text_box_label.config(background="#FFFFFF",fg="#000000")
            sep.config(background="#FFFFFF", fg="#7069DA")
            import_box_label.config(background="#FFFFFF")
            side_panel.config(background="#FFFFFF")
            help_btn.config(background="#85B1CD",highlightbackground="#85B1CD",highlightcolor="#85B1CD",highlightthickness=0)
            text_box.config(bg="grey",fg="#000000",highlightbackground="#FFFFFF",highlightcolor="#FFFFFF",highlightthickness=0)
            if tit_le == "Encrypt":
                encrypt_frame.master_pas_enctry_label.config(background="#FFFFFF",foreground="#000000")
                encrypt_frame.master_pas_enctry.config(foreground="#000000")
            else:
                pass
            if tit_le == "Decrypt":
                decrypt_frame.master_pas_entry.config(foreground="#000000")
                decrypt_frame.master_pas_entry_label.config(background="#FFFFFF",foreground="#000000")
            else:
                pass
            try:
                open.file_name_label.config(background="#FFFFFF",foreground="#000000")
            except AttributeError:
                pass

            theme = True

    # theme button
    btn = Button(root,text                      = "Dark Theme: ON",
                            background          = "#000000", 
                            foreground          = "#FFFFFF",
                            highlightcolor      = "#000518",
                            highlightbackground = "#000518",
                            highlightthickness  =1,
                            borderwidth         =0,
                            command =lambda: cmd(theme))
    btn.place(x=20,y=550)

     # theme from previous window
    if theme:
        root.config(background="#000000")
        help_btn.config(background="#000000")
        text_box_label.config(foreground="#FFFFFF",background="#121212")
        if tit_le == "Encrypt":
            encrypt_frame.master_pas_enctry_label.config(background="#121212",foreground="#FFFFFF")
            encrypt_frame.master_pas_enctry.config(foreground="#FFFFFF")
        elif tit_le == "Decrypt":
            decrypt_frame.master_pas_entry.config(foreground="#FFFFFF")
            decrypt_frame.master_pas_entry_label.config(background="#121212",foreground="#FFFFFF")
        else:
            show_error("An unexpected error occurred")
        
    else:
        btn.config(text="Dark Theme: Off")
        btn.config(background           = "#85B1CD",
                    foreground          = "#000000",
                    highlightcolor      = "#85B1CD",
                    highlightbackground = "#85B1CD")
        root.config(background="#85B1CD")
        text_box_label.config(background="#FFFFFF",foreground="#000000")
        sep.config(background="#FFFFFF", fg="#7069DA")
        import_box_label.config(background="#FFFFFF")
        side_panel.config(background="#FFFFFF")
        help_btn.config(background="#85B1CD")
        if tit_le == "Encrypt":
            encrypt_frame.master_pas_enctry_label.config(background="#FFFFFF",foreground="#000000")
            encrypt_frame.master_pas_enctry.config(foreground="#000000")
        elif tit_le == "Decrypt":
            decrypt_frame.master_pas_entry.config(foreground="#000000")
            decrypt_frame.master_pas_entry_label.config(background="#FFFFFF",foreground="#000000")
        else:
            show_error("An unexpected error occurred")

    root.mainloop()

def en_window(theme):
    window(theme,"Encrypt")

def de_window(theme):
    window(theme,"Decrypt")

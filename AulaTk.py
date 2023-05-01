from tkinter import *

window = Tk()

class Applicantion():
    def __init__(self):
        self.window = window
        self.tela()
        window.mainloop()  
           
    def tela(self):
        self.window.title("Cadastro de Clientes")
        self.window.configure(background="#bde0fe")
        self.window.geometry("700x500")
        # mexe na responsividade da Janela
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=700)
        self.window.minsize(width=400, height=300)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.window)
        # self.frame_1.place(relx=)

Applicantion()
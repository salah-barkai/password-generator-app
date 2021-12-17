import tkinter as tk
from tkinter import * 
import tkinter_page as tkp
import random



def generer_password():
    longpass= 12
    s= "abcdefghijklmnopqrstuvwxyz123456789./*"
    password="".join(random.sample(s,longpass))
    entré.delete(0,END)
    entré.insert(0,password)


window = tk.Tk()
window.title("GENERATER DE MOT DE PASSE")
window.config(bg="darkblue")
#window.icobitmap("clé(1).ico")

l1=Label(text="MOT DE PASSE")
l1.pack(pady=50)
l1.config(bg="purple",font="arial" )

entré= Entry()
entré.pack(pady=20,padx=50)

button=Button( text="Generer votre mot passe",command=generer_password)
button.pack(pady=10,padx=30)
button.config(bg="purple")

window.mainloop()
import backend as er
import ventana
from PIL import ImageTk, Image

import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("sintaxis")
window.geometry("500x600")
window.resizable(False, False)
window.config(bg="#E4FFFA")

# entrysvalue
elemento = tk.StringVar()
resultado = tk.StringVar()

# functions
def buscar():
    ventana.ventanaSecundaria(window,tk)
    pass

def sugerencias():
    lista1 = ["af","ag","b"]    
    lista2 = ["aafnganistan","plata","boro"]    
    agregarSugerencias(lista2,lista1)
    pass

def agregarSugerencias(listaElementos:list,listaSimbolos:list):

    itemsEliminar = tabla.get_children()
    for item in itemsEliminar:
        tabla.delete(item)

    for i in range(len(listaElementos)):
           tabla.insert("", 'end',text = listaElementos[i], values=(listaSimbolos[i]))



# labels
tk.Label(window,text="Biblioteca quimica",font=('Calibri', 14),background="#E4FFFA").place(x=180,y=50)
tk.Label(window,text="escribe el simbolo quimico o el nombre del elemento quimico a buscar",wraplength=480,font=('Calibri', 14),background="#E4FFFA").place(x=15,y=100)
tk.Label(window,textvariable=resultado,font=('Calibri', 14),background="#E4FFFA").place(x=200,y=550)

# entrys
tk.Entry(window,textvariable=elemento,font=('Calibri', 14),width=26).place(x=120,y=180)



# img = Image.open('./resources/sodio.png')
# img_tk = ImageTk.PhotoImage(img)
# widget = tk.Label(window, image=img_tk)
# widget.place(x=100,y=100)


# buton
tk.Button(window,font=('Calibri', 13),text="Buscar",command=buscar,width=10).place(x=275,y=230)
tk.Button(window,font=('Calibri', 13),text="Sugerencias",command=sugerencias,width=10).place(x=135,y=230)

# tabla 
tabla = ttk.Treeview(window,height=10,columns=2)
tabla.heading('#0', text='simbolo quimico',)
tabla.heading('#1', text='nombre',)
tabla.place(x=50,y=300)
window.mainloop()
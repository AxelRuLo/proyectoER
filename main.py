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

    resultado.set("")
    banderaER = er.comprobarEntrada(elemento.get().capitalize())
    if(banderaER):
        print("entro por la exprecion Regular")
        ventana.ventanaSecundaria(window,tk,elemento.get().capitalize())
    else:
        banderaNombre = er.comprobarEntradaNombre(elemento.get().capitalize())
        if(banderaNombre):
            print("entro por el nombre")
            simbolo = er.cambiarNombreSimbolo(elemento.get().capitalize())
            ventana.ventanaSecundaria(window,tk,simbolo)
        else:
            resultado.set("No se encontraron coincidencias")

def sugerencias():
    listaNombres = er.sugerenciasNombres(elemento.get().capitalize())
    listaSimbolos = er.sugerenciasElemento(elemento.get().capitalize())
    agregarSugerencias(listaNombres,listaSimbolos)


def agregarSugerencias(listaElementos:list,listaSimbolos:list):
    itemsEliminar = tabla.get_children()
    for item in itemsEliminar:
        tabla.delete(item)
    
    coincidenciasNombre = len(listaElementos)
    coincidenciaSimbolos = len(listaSimbolos)

    if(coincidenciaSimbolos>coincidenciasNombre):
        for i in range(coincidenciaSimbolos):
            if(i>coincidenciasNombre-1):
               tabla.insert("", 'end',text = " ", values=(listaSimbolos[i]))
            else:
                tabla.insert("", 'end',text = listaElementos[i], values=(listaSimbolos[i]))
    else:
        for i in range(coincidenciasNombre):
            if(i>coincidenciaSimbolos-1):
               tabla.insert("", 'end',text = listaElementos[i], values=(" "))
            else:
                tabla.insert("", 'end',text = listaElementos[i], values=(listaSimbolos[i]))
        



# labels
tk.Label(window,text="Biblioteca quimica",font=('Calibri', 14),background="#E4FFFA").place(x=180,y=50)
tk.Label(window,text="escribe el simbolo quimico o el nombre del elemento quimico a buscar",wraplength=480,font=('Calibri', 14),background="#E4FFFA").place(x=15,y=100)
tk.Label(window,textvariable=resultado,font=('Calibri', 14),background="#E4FFFA").place(x=120,y=550)

# entrys
tk.Entry(window,textvariable=elemento,font=('Calibri', 14),width=26).place(x=120,y=180)

# buton
tk.Button(window,font=('Calibri', 13),text="Buscar",command=buscar,width=10).place(x=275,y=230)
tk.Button(window,font=('Calibri', 13),text="Sugerencias",command=sugerencias,width=10).place(x=135,y=230)

# tabla 
tabla = ttk.Treeview(window,height=10,columns=2)
tabla.heading('#0', text='sugerencias con nombre',)
tabla.heading('#1', text='sugerencias en simbolo quimico ',)
tabla.place(x=50,y=300)
window.mainloop()
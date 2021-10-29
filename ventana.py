from tkinter.constants import RIGHT
import backend

def ventanaSecundaria(root,tk,simbolo):
# variables
    listaDatos = backend.obtenerDatos(simbolo)
    pesoAtomico=listaDatos[3]
    puntoFusion=listaDatos[4]
    puntoEbullicion=listaDatos[5]
    temperaturaPresion=listaDatos[6]
    configuracion=listaDatos[7]
    oxidacion=listaDatos[8]
    valencia=listaDatos[9]

    ventanaSecundaria = tk.Toplevel(root)
    ventanaSecundaria.geometry("800x700")
    ventanaSecundaria.resizable(False, False)
    ventanaSecundaria.config(bg="#E4FFFA")

    # imagen
    tk.Label(ventanaSecundaria, text = simbolo.capitalize() , font=('Calibri', 50),background="#006DF4",width=6,height=2).place(x=50,y=60)

    # labels grandes
    tk.Label(ventanaSecundaria,text=listaDatos[0],wraplength=750,font=('Calibri', 14),background="#E4FFFA").place(x=30,y=270)
    tk.Label(ventanaSecundaria,text=listaDatos[1],wraplength=750,font=('Calibri', 14),background="#E4FFFA").place(x=30,y=390)
    tk.Label(ventanaSecundaria,text=listaDatos[2],wraplength=750,font=('Calibri', 14),background="#E4FFFA").place(x=30,y=490)

    # labels chicos    
    tk.Label(ventanaSecundaria,justify=RIGHT,text=f'{pesoAtomico}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=30)
    tk.Label(ventanaSecundaria,justify=RIGHT,text=f'{puntoFusion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=60)
    tk.Label(ventanaSecundaria,justify=RIGHT,text=f'{puntoEbullicion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=90)
    tk.Label(ventanaSecundaria,justify=RIGHT,text=f'{temperaturaPresion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=120)
    tk.Label(ventanaSecundaria,justify=RIGHT,text=f'{configuracion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=150)
    tk.Label(ventanaSecundaria,justify=RIGHT,text=f'{oxidacion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=180)
    tk.Label(ventanaSecundaria,justify=RIGHT,text=f'{valencia}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=210)

    ventanaSecundaria.mainloop()



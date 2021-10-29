
def ventanaSecundaria(root,tk,simbolo):
# variables
    pesoAtomico="0"
    puntoFusion="0"
    puntoEbullicion="0"
    temperaturaPresion="0"
    configuracion="0"
    oxidacion="0"
    valencia="0"

    ventanaSecundaria = tk.Toplevel(root)
    ventanaSecundaria.geometry("800x700")
    ventanaSecundaria.resizable(False, False)
    ventanaSecundaria.config(bg="#E4FFFA")

    # imagen
    tk.Label(ventanaSecundaria, text = simbolo.capitalize() , font=('Calibri', 50),background="#006DF4",width=6,height=2).place(x=50,y=60)

    # labels grandes
    texto = "alsdfjalsdfjklasjdfñlasjdfwoerfiqruipweururoqwieuasdkljfxcmjvlkajsdlfjoiuqowéurrweirpasldfklasfdkasjdfljalñsjdfñljasdlñfjklasñdfjklñsjdfalsdfjalsdfjklasjdfñlasjdfwoerfiqruipweururoqwieuasdkljfxcmjvlkajsdlfjoiuqowéurrweirpasldfklasfdkasjdfljalñsjdfñljasdlñfjklasñdfjklñsjdf"
    tk.Label(ventanaSecundaria,text=texto,wraplength=750,font=('Calibri', 14),background="#E4FFFA").place(x=30,y=270)
    tk.Label(ventanaSecundaria,text=texto,wraplength=750,font=('Calibri', 14),background="#E4FFFA").place(x=30,y=390)
    tk.Label(ventanaSecundaria,text=texto,wraplength=750,font=('Calibri', 14),background="#E4FFFA").place(x=30,y=490)

    # labels chicos    
    tk.Label(ventanaSecundaria,text=f'Peso atomico: {pesoAtomico}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=30)
    tk.Label(ventanaSecundaria,text=f'punto de fusion: {puntoFusion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=60)
    tk.Label(ventanaSecundaria,text=f'punto de ebullicion: {puntoEbullicion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=90)
    tk.Label(ventanaSecundaria,text=f'Fase a temperatura y presión estándar: {temperaturaPresion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=120)
    tk.Label(ventanaSecundaria,text=f'configuracion electronica: {configuracion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=150)
    tk.Label(ventanaSecundaria,text=f'Estados de oxidación comunes: {oxidacion}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=180)
    tk.Label(ventanaSecundaria,text=f'Número de electrones de valencia: {valencia}',wraplength=500,font=('Calibri', 14),background="#E4FFFA").place(x=300,y=210)

    ventanaSecundaria.mainloop()



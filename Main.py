from tkinter import Tk,Button,Label,Entry,Scrollbar,Text,END,Y,LEFT,RIGHT,Frame, INSERT,X,HORIZONTAL,BOTTOM,TOP,BOTH,TRUE,NONE
from tkinter import ttk
import copy
import webbrowser
import time
import subprocess
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import xml.dom.minidom
from xml.etree import ElementTree
import os
from Nodo import Nodo
from Lista import Lista
from Evento import Evento

eventos = Lista()

def ctrlEvent(event):
    if(12==event.state and event.keysym=='c' ):
        return
    else:
        return "break"

def documento():
    path = 'ensayo.pdf'
    subprocess.Popen([path], shell=True)

def ayuda():
    ayuda = Tk()
    ayuda.title("Ayuda")
    ancho_ventana = 403
    alto_ventana = 160
    ayuda.configure(bg="#B3B3B3")
    x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ayuda.geometry(posicion)
    b1 = Button(ayuda,text="Datos del Desarrollador",command=datos,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",17))
    b1.place(x=30,y=30)
    b2 = Button(ayuda,text="Documentacion",command=documento,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",17))
    b2.place(x=100,y=90)
    ayuda.mainloop()

def datos():
    dato = Tk()
    dato.title("Datos del desarrolador")
    tk = Label(dato,text="Edwin Estuardo Reyes Reyes \n201709015\n 4to Semestre  ",bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",17))
    tk.place(x=10,y=30)
    ancho_ventana = 390
    alto_ventana = 120
    dato.configure(bg="#2D9AB7")
    x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    dato.geometry(posicion)

def carga():
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    archivo = askopenfilename(filetypes =(("Archivo XML", "*.xml"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()  
    f = open (archivo,"r") 
    mensaje = f.read()  
    Texto1.config(state='normal')
    Texto1.delete("1.0","end")
    Texto1.insert(INSERT,mensaje)
    Texto1.config(state='disable')
    f.close()
    x = 0
    state = 0
    auxiliar = ''
    palabra = ''
    while(True):
        actual = mensaje[x]
        if state == 0:
            if actual == '<':
                state = 1
                x = x + 1
            else:
                x = x + 1
        elif state == 1:   #analiza la palabra inicial
            if actual == '>' :
                if auxiliar =='EVENTOS':
                    state = 2
                    auxiliar = ''
                    x = x + 1
                else:
                    state = 0 
                    x = x + 1
                    auxiliar = ''
            else:
                auxiliar = auxiliar + actual
                x = x + 1 
        elif state == 2: 
            if actual == '<':
                state = 3
                x = x + 1
            else:
                x = x + 1
        elif state == 3:  # analiza la palabra evento
            if actual == '>':
                if auxiliar == 'EVENTO':
                    auxiliar = ''
                    state = 4
                    fecha = ''
                    reportado = ''
                    afectados = Lista()
                    error = ''
                    x = x + 1
                elif auxiliar == '/EVENTOS':
                    break
                else:
                    auxiliar = ''
                    state = 2
                    x = x + 1
            else:
                auxiliar = auxiliar + actual
                x = x + 1
        elif state == 4: #empieza a analizar en todos los eventos
            if actual == ',':
                state = 5
                x = x + 1
            else:
                x = x + 1
        elif state == 5: #analiza la fecha
            if actual == '1' or actual == '2' or actual == '3' or actual == '4' or actual == '5' or actual == '6' or actual == '7' or actual == '8' or actual == '9' or actual == '0'  or actual == '/':
                auxiliar = auxiliar + actual
                x = x + 1
            elif ord(actual) == 32:
                x = x + 1
            else:
                fecha = auxiliar
                auxiliar = ''
                x = x + 1
                state = 6
        elif state == 6: #analiza reportado
            if actual == ':':
                x = x + 1
                valido = False
                state = 7
            else:
                x = x + 1
        elif state == 7 :
            if ord(actual) == 32 or actual == '>' or actual == '<' or actual == '"':
                if valido != True:
                    auxiliar = ''
                x = x + 1
            elif ord(actual) == 10:
                reportado = auxiliar
                state = 8
                auxiliar = ''
                valido = False
            else:
                if actual == '@':
                    valido = True
                auxiliar = auxiliar + actual
                x = x + 1
        elif state == 8:    # empieza analizar usuarios afectados
            if actual == ':':
                x = x + 1
                valido = False
                state = 9
            else:
                x = x + 1
        elif state == 9 :
            #print(actual)
            #time.sleep(1)
            if ord(actual) == 32 or actual == '>' or actual == '<' or actual == '"':
                if valido != True:
                    auxiliar = ''
                x = x + 1
            elif ord(actual) == 10:
                nodo = Nodo(auxiliar)
                afectados.Agregar(nodo)
                state = 10
                auxiliar = ''
                valido = False
            elif actual == ',':
                valido = False
                nodo = Nodo(auxiliar)
                afectados.Agregar(nodo)
                x = x + 1
            else:
                if actual == '@':
                    valido = True
                auxiliar = auxiliar + actual
                x = x + 1
        elif state == 10:
            if actual == ':':
                x = x + 1
                state = 11
            else:
                x = x + 1
        elif state == 11 :
            if ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual
                x = x + 1
            elif actual == '-':
                error = auxiliar
                state = 2
                auxiliar = ''  
                nodo = Evento(fecha,reportado,afectados,error)
                nodos = Nodo(nodo)
                eventos.Agregar(nodos) 
                x = x + 1     
            else:
                x = x + 1
    print("salio")
    eventos.Print()


    
   

def enviar():
    print("")


raiz = Tk()
raiz.title("Principal")
ancho_ventana = 1280
alto_ventana = 720
raiz['bg'] = '#B3B3B3'
x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)
tamaño = 17
raiz.iconbitmap("codificacion.ico")
botonCargar = Button(raiz,text="CARGAR ARCHIVO",command=carga,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",tamaño))
botonCargar.place(x=230,y=20)
botonOperacion = Button(raiz,text="PETICIONES",bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",tamaño))
botonOperacion.place(x=550,y=20)
botonAyuda = Button(raiz,text="AYUDA",command=ayuda,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",tamaño))
botonAyuda.place(x=1150,y=20)
label1 = Label(raiz,text="ENTRADA",bg="#B3B3B3",fg="#FFFFFF",font=("Lucida Console",17))
label1.place(x=250,y=170)


botonEnviar = Button(raiz,text="ENVIAR",command=enviar,bg="#04a30c",fg="#FFFFFF",font=("Lucida Console",17))
botonEnviar.place(x=250,y=100)
botonReset = Button(raiz,text="RESET",bg="#c90d0d",fg="#FFFFFF",font=("Lucida Console",17))
botonReset.place(x=950,y=100)

frame = Frame(raiz)
frame.place(x=40,y=200)
XScroll_izquierda = Scrollbar(frame,orient='horizontal')
YScroll_izquierda = Scrollbar(frame)
XScroll_izquierda.pack(side=BOTTOM,fill=X)
YScroll_izquierda.pack(side=LEFT,fill=Y)
Texto1 = Text(frame, height=29, width=65, wrap=NONE, xscrollcommand=XScroll_izquierda.set, yscrollcommand=YScroll_izquierda.set)
Texto1.pack(side=TOP, fill=BOTH, expand=TRUE)
XScroll_izquierda.config(command=Texto1.xview)
YScroll_izquierda.config(command=Texto1.yview)
Texto1.pack(side="left")
Texto1.bind("<Key>", lambda e: ctrlEvent(e))
Texto1.config(state='disable')



label2 = Label(raiz,text="SALIDA",bg="#B3B3B3",fg="#FFFFFF",font=("Lucida Console",17))
label2.place(x=950,y=170)
fram2 = Frame(raiz)
fram2.place(x=700,y=200)
XScroll_derecha = Scrollbar(fram2,orient='horizontal')
YScroll_derecha = Scrollbar(fram2)
XScroll_derecha.pack(side=BOTTOM,fill=X)
YScroll_derecha.pack(side=LEFT,fill=Y)
Texto2 = Text(fram2,height=29,width=65, wrap=NONE, xscrollcommand=XScroll_derecha.set, yscrollcommand=YScroll_derecha.set)
Texto2.pack(side=TOP, fill=BOTH, expand=TRUE)
XScroll_derecha.config(command=Texto2.xview)
YScroll_derecha.config(command=Texto2.yview)
Texto2.pack(side="left")
Texto2.bind("<Key>", lambda e: ctrlEvent(e))
Texto2.config(state='disable')





raiz.mainloop()
from tkinter import *
import tkinter
from PIL import Image, ImageTk

#Funciones
def llenar_lista():
    print("Llenar")
def añadir_producto():
    print('Añadir')
def remover_producto():
    print('Remover')
def actualizar_producto():
    print('Actualizar')
def limpiar_texto():
    print('Limpiar')    





#Crear ventana
app = Tk()
#Titulo
app.title("Menu")
#Dimensiones
app.geometry('800x450')

#Plato

#Nombre producto
texto_nombre_producto = StringVar()

label_nombre_producto = Label(app, text='Nombre producto', font=('bold', 13)) 
label_nombre_producto.grid(row=0, column=0, pady=20)

entry_nombre_producto = Entry(app, textvariable=texto_nombre_producto)
entry_nombre_producto.grid(row=0, column=1)

#Tipo plato
texto_tipo_producto = StringVar()

label_tipo_producto = Label(app, text='Tipo producto', font=('bold', 13)) 
label_tipo_producto.grid(row=1, column=0, pady=20)

entry_tipo_producto = Entry(app, textvariable=texto_tipo_producto)
entry_tipo_producto.grid(row=1, column=1)

#Cliente
texto_cliente = StringVar()

label_cliente = Label(app, text='Cliente', font=('bold', 13)) 
label_cliente.grid(row=0, column=2)

entry_cliente = Entry(app, textvariable=texto_cliente)
entry_cliente.grid(row=0, column=3)

#Precio plato
texto_precio_producto = StringVar()

label_precio_producto = Label(app, text='Precio', font=('bold', 13)) 
label_precio_producto.grid(row=1, column=2)

entry_precio_producto = Entry(app, textvariable=texto_precio_producto)
entry_precio_producto.grid(row=1, column=3)

#Imagen
"""
imagen1 = Image.open("C:\\Users\\USER\Downloads\osaki_logo.png")
imagen2 = imagen1.resize((210,210), Image.ANTIALIAS)
test = ImageTk.PhotoImage(imagen2)
imagen1.resize
label_imagen = tkinter.Label(image=test)
label_imagen.grid(row=0, column=4, sticky=S)
"""

#Lista Productos (Listbox)
lista_productos = Listbox(app, height=8, width=70)
lista_productos.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

lista_productos.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista_productos.yview)

#Botones
btn_añadir = Button(app, text='Añadir', width=12, command=añadir_producto)
btn_añadir.grid(row=2, column=0)

btn_remover = Button(app, text='Remover', width=12, command=remover_producto)
btn_remover.grid(row=2, column=1)

btn_actualizar = Button(app, text='Actualizar', width=12, command=actualizar_producto)
btn_actualizar.grid(row=2, column=2)

btn_limpiar = Button(app, text='Limpiar', width=12, command=limpiar_texto)
btn_limpiar.grid(row=2, column=3)

#Llenar Datos
llenar_lista()



#Empezar programa
app.mainloop()

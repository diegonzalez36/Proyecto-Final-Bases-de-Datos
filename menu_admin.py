from tkinter import *
import tkinter
from PIL import Image, ImageTk
from db import Database
from tkinter import messagebox
db = Database('tienda.db')

#                     FUNCIONES

#Escribe la lista actualizada
def llenar_lista():
    lista_productos.delete(0, END)
    for fila in db.capturar():
        lista_productos.insert(END, fila)


#Añade a la tabla los datos escritos en los entrys
def añadir_producto():

    if(texto_nombre_producto.get() == '' or texto_cliente.get() == '' or texto_tipo_producto.get() == '' or texto_precio_producto.get()):
        messagebox.showerror('Campos requeridos', 'Por favor llenar todos los campos.')
        return 
    db.insertar(texto_nombre_producto.get(), texto_cliente.get(), texto_tipo_producto.get(), texto_precio_producto.get())
    lista_productos.delete(0, END)
    lista_productos.insert(END, texto_nombre_producto.get(), texto_cliente.get(), texto_tipo_producto.get(), texto_precio_producto.get())
    limpiar_texto()
    llenar_lista()



#Escribe datos del registro seleccionado en los entrys
def seleccionar_fila(event):

    try:
     global item
     index = lista_productos.curselection()[0]
     item = lista_productos.get(index) 

     entry_nombre_producto.delete(0, END)
     entry_nombre_producto.insert(END, item[1])

     entry_cliente.delete(0, END)
     entry_cliente.insert(END, item[2])

     entry_tipo_producto.delete(0, END)
     entry_tipo_producto.insert(END, item[3])

     entry_precio_producto.delete(0, END)
     entry_precio_producto.insert(END, item[4])
    except IndexError:
        pass

#Remueve algun registro seleccionado
def remover_producto():

    db.remover(item[0])
    limpiar_texto()
    llenar_lista()


#Actualiza algun cambio en el registro
def actualizar_producto():

    db.actualizar(item[0], texto_nombre_producto.get(), texto_cliente.get(), texto_tipo_producto.get(), texto_precio_producto.get())
    llenar_lista()

#Limpia texto de las entradas
def limpiar_texto():
    
    entry_nombre_producto.delete(0, END)
    entry_cliente.delete(0, END)
    entry_tipo_producto.delete(0, END)
    entry_precio_producto.delete(0, END)
    


#                     INTERFAZ


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

#Unir seleccion
lista_productos.bind('<<ListboxSelect>>', seleccionar_fila)

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

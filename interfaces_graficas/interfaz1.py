# importando toda la libreria de tkinter
from tkinter import  *

# Creando la raiz de la interfaz
root = Tk()

# cambio de titulo de la venta
root.title('Primera interfaz con PY y TK')

# Definimos si sera posible redimencionar la interfaz , por defecto es (1,1) (x, y)
root.resizable(1,1)  # 0, 0 deshabilita en ambos sentidos

# Cambio del icono , en .ico
root.iconbitmap('logo-py.ico')


# Creamos un fram(variable root)
frame = Frame(root)
# le indica que se enpaquete y se distribuya dentro del root
# side='right'  se le indica la alineacion al contendor
# fill='both' el frame se ajustara al la redimencion del padre, y expand permite en el eje y
frame.pack(fill='both',  expand=1)
# se configura por defailt el ancho y alto,
# cursor="pirate" => cursor cambia el tipo de curso
frame.config(width=480, height=600)
# cambia el bacnground color del frame
frame.config(bg="lightgreen")


# Crea la etiqueta  Label(frame o marco, texto)
# .place(posicion en x, posicion en y)
Label(frame, text="Hola Mundo").place(x=100, y=100)
Label(frame, text="Hola Mundo 2").place(x=100, y=130)
# Etiqueta personalizada
label1 = Label(frame, text="Hola Mundo 3")
label1.config(bg="green", fg="blue", font=("Verdana", 25))
label1.place(x=100, y=170)

# Etiqueta con valor a partir deuna variable
label2 =  Label(frame)
# Creando una variable de tipo StringVar()
valorLabel2 = StringVar()
valorLabel2.set("Hola Mundo 4 Dinamico")
label2.config(textvariable=valorLabel2)
label2.place(x=100, y=220)

# Imagen
imagen1 = PhotoImage(file='logo-py.png')
# ponemos la imagen en un label
Label(frame, image=imagen1, bd=0).place(x=300, y=300)

# Campos input
entry = Entry(frame)
entry.config(justify='center', show='*')
entry.place(x=0, y=50)

# Usando el grid
# se comporta como el pack, posciion los widgets y redimenciona la ventana
label3 = Label(frame, text="Nombre :")
label3.grid(row=0, column=0)
entry2 = Entry(frame)
entry2.grid(row=0, column=1)


#Campo de texto , como un textarea
texto1 = Text(frame)
texto1.place(x=500, y=0)
# width = cantidad caracteres horizontal , height = cantidad de lineas
texto1.config(width=100, height=10, font=('Consolas', 25), selectbackground='red')


# Botones
def hola_mundo():
    print("Hola Mundo")

def crear_label():
    Label(frame, text="Imprimiendo Label").place(x=0, y=600)


    #Button(Ubicacion, text=texto del boton, command=callback fuction)
Button(frame, text="Click en mi", command=crear_label).place(x=0, y=500)




# estas funcionan tambien desde el root.config( pero modiufica el root)
root.config(width=500, height=400, cursor='pirate', bg='lightblue')
# Crea la base del proyecto y debe ir al final de la interfaz
root.mainloop()
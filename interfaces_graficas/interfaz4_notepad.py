from tkinter import *
from tkinter import filedialog
from io import open

# Ruta global para almacenar la ruta del fichero
ruta = ""


# Funciones accion
def nuevo():
    # con global le especifica que estamos usando la variable global
    global ruta
    ruta = ""
    # Le indicamos que el primer caracter al final elimine todos los valores
    texto.delete(1.0, "end")


def abrir():
    global ruta
    # esepcificja la ruta actual, y le asginamos el valor
    ruta = filedialog.askopenfilename(title='Abrir fichero', initialdir='.', filetype=(('Ficheros de texto', '*.txt'),))
    print("ruta", ruta)
    # Si se selecciono algun archivo llega != null
    if ruta != '':
        # abrimos el archivo
        fichero = open(ruta, 'r')
        # capturamos el texto
        contenido = fichero.read()
        # eliminamos el contenido de existir
        texto.delete(1.0, 'end')
        # insertamos el texto
        texto.insert('insert',contenido)
        # cerramos el fichero
        fichero.close()
        # Cambiamos el nombre de la ventana principal
        root.title(ruta + " - GM Notepad")

def guardar():
    global ruta
    mensajeMonitor.set('Guardar fichero')
    if ruta != "":
        # capturamos el valor desde el caracter 1 hasta el final, menis el ultimo caracter que es un salto de linea
        contenido = texto.get(1.0, 'end-1c')
        print("ruta guardar", ruta)
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensajeMonitor.set('Fichero guardado')
    else:
        guardar_como()



def guardar_como():
    global ruta
    # Seleccionar directorio donde guardara el archivo
    fichero = filedialog.asksaveasfile(title='Guardar fichero', mode='w', defaultextension='.txt')
    print("fichero guardar_como", fichero)
    if fichero is not None:
        ruta = fichero.name  # le setemasmo la ruta actual
        print("ruta guardar_como", ruta)
        # capturamos el valor desde el caracter 1 hasta el final, menis el ultimo caracter que es un salto de linea
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensajeMonitor.set('Fichero guardado')
    else:
        mensajeMonitor.set('Guardado cancelado')
        ruta = ''


root = Tk()
root.title('Notepad GM')

# Menu Superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Nuevo', command=nuevo)
filemenu.add_command(label='Abrir', command=abrir)
filemenu.add_command(label='Guardar', command=guardar)
filemenu.add_command(label='Guardar como', command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)

# añadiendo opciones
menubar.add_cascade(menu=filemenu, label='Archivo')

# Caja de texto central
texto = Text(root)
texto.pack(fill='both', expand=1)
texto.config(bd=0, padx=6, pady=4, font=('Consolas', 12))

# Label de estatus
mensajeMonitor = StringVar()
mensajeMonitor.set('Bienvenido a GM Notepad')
monitor = Label(root, textvar=mensajeMonitor, justify='left')
monitor.pack(side='left')

root.config(menu=menubar)
root.mainloop()

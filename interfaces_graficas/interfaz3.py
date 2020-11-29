from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()


# ///////////PopUps ventanas emergentes
def test():
    #MessageBox.showinfo(title='Titulo', message='Contenido del mensaje')
    #MessageBox.showwarning(title='Titulo Alerta', message='Contenido del mensaje alerta')
    #MessageBox.showerror(title='Titulo Error', message='Contenido del mensaje error')

    #resultadoPregunta = MessageBox.askquestion(title='Titulo Error de la pregunta', message='Contenido del mensaje pregunta')
    #print("resultadoPregunta",resultadoPregunta)

    #resultadoPregunta = MessageBox.askokcancel(title='Titulo Error de la pregunta', message='Contenido del mensaje pregunta')
    #print("resultadoPregunta",resultadoPregunta)

    #resultadoPregunta = MessageBox.askyesno(title='Titulo Error de la pregunta',message='Contenido del mensaje pregunta')
    #print("resultadoPregunta", resultadoPregunta)

    resultadoPregunta = MessageBox.askretrycancel(title='Reintentar',message='Contenido del mensaje pregunta')
    print("resultadoPregunta", resultadoPregunta)


#//////////// Color chooser
def selec_color():
    color = ColorChooser.askcolor(title='Elige un color')
    print("color", color)


#//////////// Filte Dialog
def select_file():
    # Abre la ventana para saleeccionar del navegaor el fichero
    #ruta = FileDialog.askopenfile(title='Abrir un fichero')
    # especificando path inicial que abra la ventana, y el tipo de ficheros a visualizar o permitir
    ruta = FileDialog.askopenfile(title='Abrir un fichero', initialdir='C:', filetypes=(("Fciheros de text", '*.txt'),('Ficheros excel', '*.xlsx') ))
    print("ruta",ruta)

    # Sirve para abrir o crear un archivo y guardarlo
    file = FileDialog.asksaveasfile(title='Guardar archivo', mode='w', defaultextension='.txt')
    print("file", file)


#//////// menu principal
# Menus superiores
menubar = Menu(root)  #  no se empaqueta

# se debe pasar al root de la siguiente forma
root.config(menu=menubar)

# Añadiendo hijos del menu principal
#tearoff=0  elimina la opcion por default --
filemenu = Menu(menubar, tearoff=0)
# Añadimos las opciones adicionales
filemenu.add_command(label='Alerta PopUp', command=test)
filemenu.add_command(label='Color', command=selec_color)
filemenu.add_command(label='Selecciona fichero', command=select_file)
filemenu.add_command(label='Cerrar')
# dibuja una barra de separacion
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Copiar')
editmenu.add_command(label='Pegar')

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='AyudAcerca de..')

#Genenerandop el menu en cascada con las opciones
menubar.add_cascade(label='Archivo', menu=filemenu)
menubar.add_cascade(label='Editar', menu=editmenu)
menubar.add_cascade(label='Ayuda', menu=helpmenu)







root.mainloop()

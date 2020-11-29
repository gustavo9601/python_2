# importando toda la libreria de tkinter
from tkinter import *

# Creando la raiz de la interfaz
root = Tk()

n1 = StringVar()
n2 = StringVar()
resultado = StringVar()
Entry(root, justify='center', textvariable=n1).pack()
Entry(root, justify='center', textvariable=n2).pack()
Entry(root, justify='center', textvariable=resultado, state='disabled').pack()


def suma():
    #Moficando el valor del campo
    resultado.set(float(n1.get()) + float(n2.get()))

Button(root, text='Sumar', command=suma).pack()


#Radio button

def valor_Seleccionado():
    valor_Seleccion.config(text=f"Valor: {variableComun.get()}")

variableComun = IntVar()

Radiobutton(root, text='Opcion 1', variable=variableComun, command=valor_Seleccionado, value=1).pack()
Radiobutton(root, text='Opcion 2', variable=variableComun, command=valor_Seleccionado, value=2).pack()
Radiobutton(root, text='Opcion 3', variable=variableComun, command=valor_Seleccionado, value=3).pack()
Label(root, text="Valor del radio button").pack()
valor_Seleccion = Label(root)
valor_Seleccion.pack()

def resetRadioButton():
    variableComun.set(None)
    valor_Seleccion.config(text='')

Button(root, text="Reiniciar RadioButton", command=resetRadioButton).pack()


# Check Buttons
leche = IntVar() # 1 si , 0 no
azucar = IntVar() # 1 si , 0 no

Label(root, text='Como quieres el cafe ?').pack()
# onvalue => valor cuando este cliqueado, offvalue => valor cuando este deschuliado
Checkbutton(root, text="Con leche", variable=leche, onvalue=1, offvalue=0).pack()
Checkbutton(root, text="Con azucar", variable=azucar, onvalue=1, offvalue=0).pack()


# Crea la base del proyecto y debe ir al final de la interfaz
root.mainloop()

from tkinter import *
from restaurante_bd import ConectionRestaurante

root = Tk()
root.title('Restaurante GM')

# Menu Superior
Label(root, text="Restaurante GM", font=("Verdana", 25)).pack()
Label(root, text="Menu del dia", font=("Verdana", 20)).pack()

restaurante = ConectionRestaurante()
menu = restaurante.query_platos()

for menu in menu:
    Label(root, text=str(menu[1]), font=("Verdana", 15)).pack()
    platos = menu[2].split(',')
    for idx,plato in enumerate(platos):
        texto = str((idx + 1)) + ' - ' + plato
        Label(root, text=texto, font=("Verdana", 10)).pack()


root.config(bg="lightgreen")
root.mainloop()

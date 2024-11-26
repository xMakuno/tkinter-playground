import tkinter as tk

root = tk.Tk()

# Tamanio del cosito
root.geometry("400x400")

# "Label" o etiqueta, es un texto. Este puede tener varios parametros como el texto, el color de fondo,tipo de letra
LoginTitle = tk.Label(root, text="¡Bienvenido!", bg="aqua")
# Esto es para mostrar el objeto o cosito.
LoginTitle.pack()

"""
Usualmentes, cuando ocupamos pack(),
los objetos se muestran en orden que se hicieron pack(), si tengo:

cosito1.pack()
cosito2.pack()
cosito3.pack()

en la app voy a ver el orden

cosito1
cosito2
cosito3

si tengo:

taco = algo
mario = algo

y hago:

mario.pack()
taco.pack()

voy a ver:

mario
taco

a pesar de crear taco primero y luego mario

"""

# Durante la programacion de codigo de aplicaciones, los objetos (variables) suelen tener nombres largos para poder identificarlos
# de una manera facil
CarnetLabel = tk.Label(root, text="Carnet de Estudiante")
# Mostrar objeto
CarnetLabel.pack()
# Si yo le pongo un valor al paracmetro de pady (significa padding y) dentro de pack() lo que hace es poner espacio vacio 
# CarnetLabel.pack(pady=5)


ContrasenaLabel = tk.Label(root, text="Contraseña")
ContrasenaLabel.pack()
# ContrasenaLabel.pack(pady=5)

LoginButton = tk.Button(root, text="Iniciar Sesion")
LoginButton.pack()
# LoginButton.pack(pady=5)

root.mainloop()

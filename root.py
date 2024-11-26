import tkinter as tk

# Objeto principal
root = tk.Tk()
# Titulo de la aplicacion principal
root.title("Cafeteria ESEN")

hello_text = tk.Label(root,text="Hello!")
hello_text.pack()

# Nombre de variable = tk.<Elemento>( contenedor o papa, paramentro1 = valor, parametro2 = valor, parametro3 = valor....)
hello_btn = tk.Button(root, text="Hello World!")
# # "Mostrar" en root 
hello_btn.pack()

# Inicie la aplicacion o algo asi
root.mainloop()
import tkinter as tk

root = tk.Tk()
"""

GRID en vez de pack
tiene varios parametros pero normalmente recibe lo siguiente:

objeto.grid(row=#, column=#)

  0       1 
0 cosito1 cosito2
1 cosito3 cosito4

      0       1       2       3
row 0 cosito1 cosito2 cosito3 cosito 4

cosito1.grid(row=0,column=0)
cosito2.grid(row=0,column=1)
cosito3.grid(row=0,column=2)
cosito4.grid(row=0,column=3)

"""
cosito1 = tk.Label(root, text="cosito1", borderwidth=1, relief="solid")
# cosito1.grid(row=0,column=0)

cosito2 = tk.Label(root, text="cosito2", borderwidth=1, relief="solid")
cosito2.grid(row=0,column=1)

cosito3 = tk.Label(root, text="cosito3", borderwidth=1, relief="solid")
cosito3.grid(row=1,column=0)

cosito4 = tk.Label(root, text="cosito4", borderwidth=1, relief="solid")
cosito4.grid(row=1,column=1)

"""
WEIGHT
  0 1
0 1 1 
1 1 1
Parte 100cm -> 2 partes, y cada parte mide 100cm / 2 -> 2 partes de 50cm que va a ser 60cm


= = =
"""
# recibe como parametros el Index (#) de fila y su peso
# si root tiene 200cm y row 1 tiene 1 parte, row 2 tiene 1 parte
# en total, hay 2 partes
# cada parte 200cm/2 = 100cm
# row 1 = 100cm
# row 2 = 100cm

# Filas
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Columnas
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
"""
STICKY
    N
    |
    |
W ====== E
    |
    |
    S
"""
# cosito1.grid(row=0,column=0, sticky="nsew")
cosito1.grid(row=0,column=0, sticky="nsew")
cosito2.grid(row=0,column=1, sticky="nsew")
cosito3.grid(row=1,column=0, sticky="nsew")
cosito4.grid(row=1,column=1, sticky="nsew")

"""
ROWSPAN
COLUMNSPAN
"""

cosito5 = tk.Label(root, text="cosito5")
# cosito5.grid(row=0,column=0, columnspan=2, sticky="nsew")
cosito5.grid(row=0,column=0, rowspan=2, sticky="nsew")

root.mainloop()
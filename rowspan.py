import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a grid with labels for demonstration
for i in range(3):
    for j in range(3):
        tk.Label(root, text=f"{i*3 + j + 1}", borderwidth=1, relief="solid").grid(row=i, column=j, sticky="nsew")

# Make the grid responsive
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Place a widget that spans cells 2 and 5 (column 1, row 0 and row 1)
span_label = tk.Label(root, text="Hi", bg="lightgreen", borderwidth=1, relief="solid")
span_label.grid(row=0, column=1, rowspan=2, sticky="nsew")

root.mainloop()

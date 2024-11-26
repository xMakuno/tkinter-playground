import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create labels with different sticky options
# tk.Label(root, text="Top (north)", bg="lightblue").grid(row=0, column=0, sticky="n")  # Top of the cell
# tk.Label(root, text="Bottom (south)", bg="lightgreen").grid(row=1, column=0, sticky="s")  # Bottom of the cell
# tk.Label(root, text="Left (west)", bg="lightcoral").grid(row=2, column=0, sticky="w")  # Left of the cell
# tk.Label(root, text="Right (east)", bg="lightyellow").grid(row=3, column=0, sticky="e")  # Right of the cell


tk.Label(root, text="Stretch horizontally", bg="lightblue").grid(row=0, column=0, sticky="ew")  # Stretches across East and West
tk.Label(root, text="Stretch vertically", bg="lightgreen").grid(row=1, column=0, sticky="ns")  # Stretches across North and South
tk.Label(root, text="Stretch in both directions", bg="lightcoral").grid(row=2, column=0, sticky="nesw")  # Stretches across all directions


root.mainloop()

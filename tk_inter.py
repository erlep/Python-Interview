#!/usr/bin/env python

#  ===============================================
#   tkinter - example
#  ===============================================

import tkinter as tk

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Moje první Tkinter aplikace")

# Přidání štítku
label = tk.Label(root, text="Ahoj, světe!")
label.pack()

# Spuštění hlavní smyčky
root.mainloop()

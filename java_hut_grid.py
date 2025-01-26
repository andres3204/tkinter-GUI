# Andres Jimenez
# Jan 29, 2025
# Using grid to make the GUI

import tkinter as tk

root = tk.Tk()
root.title("Java Hut")
root.geometry("280x280")
root.resizable(False, False)

# Frame One
frameOne = tk.LabelFrame(root, text="Size", padx=5, pady=5)
frameOne.grid(padx=10, pady=10, column=0, row=0, ipadx=10, ipady=10)

radioSize = tk.StringVar()
radioS = tk.Radiobutton(frameOne, text="Small",  variable=radioSize, value="Option 1")
radioM = tk.Radiobutton(frameOne, text="Medium", variable=radioSize, value="Option 2")
radioL = tk.Radiobutton(frameOne, text="Large",  variable=radioSize, value="Option 3")
radioS.grid(padx=5, pady=5, sticky="w")
radioM.grid(padx=5, pady=5, sticky="w")
radioL.grid(padx=5, pady=5, sticky="w")

# Frame Two
frameTwo = tk.LabelFrame(root, text="Extras", padx=5, pady=5)
frameTwo.grid(padx=10, pady=10, column=1, row=0, ipadx=10, ipady=27)

radioCream = tk.Checkbutton(frameTwo, text="Cream")
radioSugar = tk.Checkbutton(frameTwo, text="Sugar")
radioCream.grid(padx=5, pady=5, sticky="w")
radioSugar.grid(padx=5, pady=5, sticky="w")

# Total Label
total = tk.Label(root, text="Total:")
total.grid(row=1, column=0, columnspan=2)

# Text
text = tk.Entry(root)
text.grid(padx=10, row=2, column=0, columnspan=2, sticky="EW")

# Place Order Button
placeOrder = tk.Button(root, text="Place Order")
placeOrder.grid(padx=10, row=3, column=0, columnspan=2, sticky="EW")

root.mainloop()
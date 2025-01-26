# Andres Jimenez
# Jan 29, 2025
# Using place to make the GUI

import tkinter as tk

root = tk.Tk()
root.title("Java Hut")
root.geometry("280x240")
root.resizable(False, False)

# Frame One
frameOne = tk.LabelFrame(root, text="Size")
frameOne.place(x=10, y=10, width=120, height=120)

radioSize = tk.StringVar()
radioS = tk.Radiobutton(frameOne, text="Small",  variable=radioSize, value="Option 1")
radioM = tk.Radiobutton(frameOne, text="Medium", variable=radioSize, value="Option 2")
radioL = tk.Radiobutton(frameOne, text="Large",  variable=radioSize, value="Option 3")
radioS.place(x=20, y=20, width=70, height=20)
radioM.place(x=20, y=40, width=85, height=20)
radioL.place(x=20, y=60, width=70, height=20)

# Frame Two
frameTwo = tk.LabelFrame(root, text="Extras")
frameTwo.place(x=140, y=10, width=120, height=120)

radioCream = tk.Checkbutton(frameTwo, text="Cream")
radioSugar = tk.Checkbutton(frameTwo, text="Sugar")
radioCream.place(x=20, y=20, width=70, height=20)
radioSugar.place(x=20, y=40, width=70, height=20)

# Total Label
total = tk.Label(root, text="Total:")
total.place(x=100, y=140, width=70, height=25)

# Text
text = tk.Entry(root)
text.place(x=10, y=160, width=250, height=25)

# Place Order Button
placeOrder = tk.Button(root, text="Place Order")
placeOrder.place(x=10, y=180, width=250, height=25)

root.mainloop()
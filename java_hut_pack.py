# Andres Jimenez
# Jan 29, 2025
# Using pack to make the GUI
# Used AI for topFrame & bottomFrame. I was not being able to have total, text, and placeOrder below the two frames.

import tkinter as tk

root = tk.Tk()
root.title("Java Hut")
root.geometry("280x250")
root.resizable(False, False)

# Top Frame for Size and Extras
topFrame = tk.Frame(root)
topFrame.pack(side="top", padx=10, pady=5)

# Frame One
frameOne = tk.LabelFrame(topFrame, text="Size", padx=5, pady=5)
frameOne.pack(padx=10, pady=5, anchor="n", side="left", expand=0)

radioSize = tk.StringVar()
radioS = tk.Radiobutton(frameOne, text="Small",  variable=radioSize, value="Option 1")
radioM = tk.Radiobutton(frameOne, text="Medium", variable=radioSize, value="Option 2")
radioL = tk.Radiobutton(frameOne, text="Large",  variable=radioSize, value="Option 3")
radioS.pack(padx=5, pady=5, anchor="w")
radioM.pack(padx=5, pady=5, anchor="w")
radioL.pack(padx=5, pady=5, anchor="w")

# Frame Two
frameTwo = tk.LabelFrame(topFrame, text="Extras", padx=5, pady=5)
frameTwo.pack(padx=10, pady=5, anchor="n", ipadx=10, ipady=17, side="left", expand=False)

radioCream = tk.Checkbutton(frameTwo, text="Cream")
radioSugar = tk.Checkbutton(frameTwo, text="Sugar")
radioCream.pack(padx=5, pady=5, anchor="w")
radioSugar.pack(padx=5, pady=5, anchor="w")

# Frame for Total, Text, and Place Order
bottomFrame = tk.Frame(root)
bottomFrame.pack(side="top", pady=10)

# Total Label
total = tk.Label(bottomFrame, text="Total:")
total.pack(side="top")

# Text
text = tk.Entry(bottomFrame)
text.pack(side="top")

# Place Order Button
placeOrder = tk.Button(bottomFrame, text="Place Order")
placeOrder.pack(side="top")

root.mainloop()
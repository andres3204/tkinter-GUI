# Andres Jimenez
# Jan 29, 2025
# Layout for qwixx game. Not functional but able to show the GUI functionality.

import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk

def exit():
    root.destroy()

#intialize root
root = tk.Tk()
root.title("Qwixx Game")
root.geometry("900x400")
#root.resizable(False, False)

# Menu
menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Exit", command=exit)
menuBar.add_cascade(label="File", menu=fileMenu)
root.config(menu=menuBar)

# Frame for game
frame = tk.Frame(root)
frame.pack(side="top", padx=10, pady=10)

# Colors for rows
colors = ["red", "yellow"]
colors2 = ["green", "blue"]

# Rows for colors
for index, color in enumerate(colors):
    rowFrame = tk.Frame(frame)
    rowFrame.grid(row=colors.index(color), column=0, padx=10, pady=5, sticky="w")

    # Label for colors
    colorLabel = tk.Label(rowFrame, text=color.capitalize(), bg=color, fg="black", width=10)
    colorLabel.pack(side="left", padx=5)

    # Number in boxes for that row
    for i in range(2, 13):
        numberBox = tk.Button(rowFrame, text=str(i), width=2, relief="solid", bg=color, fg="black")
        numberBox.pack(side="left", padx=2)
    
    # Add lock button for first two rows
    lockButton = tk.Button(rowFrame, text="🔒", bg=color, activebackground="lightgray")
    lockButton.pack(side="left", padx=5)

for index, color in enumerate(colors2):
    rowFrame = tk.Frame(frame)
    rowFrame.grid(row=index + len(colors), column=0, padx=10, pady=5, sticky="w")

    # Label for colors2
    colorLabel = tk.Label(rowFrame, text=color.capitalize(), bg=color, fg="black", width=10)
    colorLabel.pack(side="left", padx=5)

    # Number in boxes for those rows. Logic with help from AI.
    for i in range(12, 1, -1):
        numberBox = tk.Button(rowFrame, text=str(i), width=2, relief="solid", bg=color, fg="black")
        numberBox.pack(side="left", padx=2)
    
    # Add lock button for two last rows
    lockButton = tk.Button(rowFrame, text="🔒", bg=color, activebackground="lightgray")
    lockButton.pack(side="left", padx=5)

# Add penalties section on the right
penaltyFrame = tk.Frame(frame)
penaltyFrame.grid(row=6, column=0, columnspan=4, padx=20, pady=5, sticky="ne")

image = Image.open("score.png")
resizedImage = image.resize((560, 100), Image.LANCZOS)
photo = ImageTk.PhotoImage(resizedImage)
imgLabel = tk.Label(penaltyFrame, image=photo)
imgLabel.pack(pady=5, side="left")

# Penalties Label
penaltyLabel = tk.Label(penaltyFrame, text="Penalties")
penaltyLabel.pack(pady=5)

# Penalties
penaltyEntries = []
for i in range(4):
    penaltyButton = tk.Checkbutton(penaltyFrame, width=2)
    penaltyButton.pack(side="left", pady=5)
    penaltyEntries.append(penaltyButton)

# Bottom Frame for total points
bottomFrame = tk.Frame(root)
bottomFrame.pack(pady=20)

# Score Total Label
totalLabel = tk.Label(bottomFrame, text="Total:")
totalLabel.pack(padx=10, side="left")

scoreEntries = []
for i in range(6):
    scoreText = tk.Entry(bottomFrame, width=5, justify="center")
    scoreText.pack(side="left", padx=5)
    scoreEntries.append(scoreText)
    if i < 3:  # Add "+" between entries, but not after the last one
        plusLabel = tk.Label(bottomFrame, text="+", width=2)
        plusLabel.pack(side="left", padx=2)
    elif i == 3 and i < 4:
        minusLabel = tk.Label(bottomFrame, text="-", width=2)
        minusLabel.pack(side="left", padx=2)
    elif i == 4 and i < 5:
        equalLable = tk.Label(bottomFrame, text="=", width=2)
        equalLable.pack(side="left", padx=2)
    else:
        SyntaxError

# Run App
root.mainloop()
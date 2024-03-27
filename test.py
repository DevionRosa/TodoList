import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Dropdown on Canvas")

# Create a canvas
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Create a StringVar to store the selected option
selected_option = tk.StringVar()

# Function to handle option selection
def handle_selection(event):
    print("Selected option:", selected_option.get())

# Create a dropdown options box (combobox)
options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(root, values=options, textvariable=selected_option)
combobox.bind("<<ComboboxSelected>>", handle_selection)

# Add the combobox to the canvas
canvas.create_window(100, 50, window=combobox, anchor="center")

root.mainloop()

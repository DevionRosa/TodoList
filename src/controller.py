import tkinter as tk
from tkinter import ttk
from task import tasks
from tasklist import tasklists
#def save_and_exit():
    
def tasklistpage():
    taskcanvas.pack_forget()
    canvas.pack()
    button.pack(side = tk.BOTTOM)
    button.config(text = "Add task", command = addtaskwindow)
    
def addtaskwindow():
    canvas.pack_forget()
    taskcanvas.pack()
    button.pack(side = tk.BOTTOM)
    button.config(text = "Save and Exit", command = tasklistpage)
    
# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a canvas widget
canvas = tk.Canvas(window, width=500, height=800, bg='white')
canvas.pack()

#create task canvas
taskcanvas = tk.Canvas(window, width=500, height=800, bg='lightblue')

#creates input boxes for the taskcanvas
title_input = tk.Entry(window) 
title_window = taskcanvas.create_window(250, 100, window=title_input, width=400)

desc_input = tk.Text(window, wrap=tk.WORD, height=4)  # 'wrap=tk.WORD' ensures it wraps at word boundaries
desc_window = taskcanvas.create_window(250, 200, window=desc_input, width=400, height=100)

# Create a dropdown options box (combobox)
selected_option = tk.StringVar()
options = ["Low Priority", "Medium Priority", "High Priority"]
combobox = ttk.Combobox(window, values=options, textvariable=selected_option)
combobox.bind("<<ComboboxSelected>>")

# Add the combobox to the canvas
taskcanvas.create_window(120, 130, window=combobox, anchor="center")

#adds button
button = tk.Button(window, text="Add Task", command = addtaskwindow)
button.pack(side = tk.BOTTOM)

window.mainloop()
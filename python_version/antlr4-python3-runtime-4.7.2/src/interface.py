from tkinter import BOTH, END, LEFT, Menu
import tkinter as tk
import tkinter.scrolledtext as scrolledtext

import index 

# from tkinter import *

window = tk.Tk()
window.title("CMSC 227 - Advanced Database Systems")
window.geometry("500x700")

#------FUNCTIONS-------
def execute_sql_command(command):
   x = 0

def input_sql_command():

    # gets the SQL command
    command = str(input_text_field.get('1.0', END))
    input_text_field.delete('1.0', END) # delete text
    input_text_field.update() 

    # output = index.main(command)
    # print(output)

    #insert output
    output_text_field.insert(tk.END, command) 
    # autoscroll
    output_text_field.see("end") 

# does nothing for now
def import_csv():
   x = 0

#-------Labels-----

#-------Entry fields-----

# Menubar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Import CSV", command=import_csv)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
window.config(menu=menubar)

# Text Fields
input_text_field = tk.Text(master=window, height=10, width=30)
# input_text_field.grid(column=0,row=0).pack(fill=tk.BOTH)

# Button
button1 = tk.Button(text="Execute SQL", command=input_sql_command)
button1.grid(column=1,row=0)

# output text field
output_text_field = scrolledtext.ScrolledText(master=window, height=20, width=40, undo=True)
output_text_field.grid(column=0,row=2)

window.mainloop()

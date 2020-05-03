# python program to create a simple TODO list

# import everything from tkinter
from tkinter import *
from tkinter import Listbox

# create a GUI window
window = Tk()
# give title to the window
window.title("TODO-list")

# create a list to store tasks
content = Listbox(window, font="Ariel 24 bold")
# create an instance of the variable class
task = StringVar()
# create a text entry box to write tasks
e = Entry(window, textvariable=task, font="Ariel 24")
# create a button named ADD which when clicked command affiliated to it is executed
add = Button(window, text="ADD", font="Ariel 20", padx=30,
             command=lambda content=content, task=task: content.insert(END, task.get()))
# create a button named DELETE which when clicked command affiliated to it is executed
delete = Button(window, text="DELETE", font="Ariel 20",
                command=lambda content=content: content.delete(ANCHOR))

# grid places our widgets in a table by dividing our window in row and columns
content.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
e.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
add.grid(row=2, column=0, padx=5, pady=20)
delete.grid(row=2, column=1, padx=5, pady=20)

# display the window
window.mainloop()
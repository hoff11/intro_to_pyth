#! Python 3.4
"""
File Parser
"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = Tk(  )

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(filetypes =(("Mod File", "*.mod"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (type(name))
    Label(root, textvariable=name).pack()

    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


Title = root.title( "File Opener")
label = ttk.Label(root, text ="Choose a file to parse!!!",foreground="red",font=("Helvetica", 16))
label.pack()

b = Button(root, text="OK", command=OpenFile)
b.pack()
#Menu Bar
menu = Menu(root)
root.config(menu=menu)
file = Menu(menu)
file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())
menu.add_cascade(label = 'File', menu = file)

root.resizable(width=True, height=True)
root.geometry('{}x{}'.format(1000, 800))
root.mainloop()


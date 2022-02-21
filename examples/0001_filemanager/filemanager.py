import sys
sys.path.append('../../src')

from NeoViki_UI_Tk import *
from tkinter import filedialog

FILE_TYPES=[('PDF files', '.pdf'),
            ('JPG files', '.jpg'),
            ('PNG files', '.png'),
            ('Py files', '*.py'),
            ('all files', '.*')]

def open_folder():
    global root
    rep = filedialog.askdirectory(
        parent=root.handle,
        initialdir=os.getcwd())
    print(rep)

def open_file():
    global root
    rep = filedialog.askopenfilenames(parent=root.handle, initialdir=os.getcwd(), filetypes=FILE_TYPES)
    print(rep[0])


root = BEGIN()
root.title = "demo"
root.width=500
root.height = 300
#root.color.bg = '#555'
root.gotoxy(200,100)

b1 = button(root)
b1.width = 60
b1.height = 5
b1.font.size = 12
b1.write("Open Folder")
b1.callback(open_folder)
b1.gotoxy(200, 100)

b2 = button(root)
b1.width = 60
b1.height = 5
b2.font.size = 12
b2.write("Open File")
b2.callback(open_file)
b2.gotoxy(200, 150)

#obj.disable()
#obj.enable()

END(root)


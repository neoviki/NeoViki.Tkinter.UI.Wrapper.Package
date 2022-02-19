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
        parent=root.object,
        initialdir=os.getcwd())
    print(rep)

def open_file():
    global root
    rep = filedialog.askopenfilenames(parent=root.object, initialdir=os.getcwd(), filetypes=FILE_TYPES)
    print(rep[0])


root = BEGIN()
root.title("demo")
root.dimension(500,300)
#root.bg('#555')
root.gotoxy(200,100)

b1 = button(root)
b1.dimension(60, 5)
b1.gotoxy(200, 100)
b1.font_size(12)
b1.write("Open Folder")
b1.callback(open_folder)

b2 = button(root)
b2.dimension(60, 5)
b2.gotoxy(200, 150)
b2.font_size(12)
b2.write("Open File")
b2.callback(open_file)

#obj.disable()
#obj.enable()

END(root)


import sys
sys.path.append('../../src')

from NeoViki_UI_Tk import *

from tkinter import filedialog
import time
import threading


FILE_TYPES=[('PDF files', '.pdf'),
            ('JPG files', '.jpg'),
            ('PNG files', '.png'),
            ('Py files', '*.py'),
            ('all files', '.*')]

cb_thread=None
ui_exit=False

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

def callback_func_threaded():
    cb_thread = threading.Thread(target=callback_func)
    cb_thread.start()

def callback_func():
    global obj_progress, cb_thread
    obj_progress.start()
    for i in range(10):
        time.sleep(1)
        print(str(i)+"\n")
    obj_progress.stop()
    cb_thread=None

def main():
    global obj_progress, ui_exit
    root = BEGIN()
    root.title = "demo"
    root.dimension(500,500)
    root.bg = 'green'
    root.gotoxy(200,100)

    i = logo(root)
    i.dimension(200, 50)
    i.path = 'logo_200x50.png'
    i.gotoxy(20,10)
    #obj.update(1)
    #bj.vertical()

    #obj.disable()
    #obj.enable()

    END(root)

    if cb_thread:
        cb_thread.exit()
        cb_thread.join()

    os._exit(0)


main()

'''
    Python UI Library based on Tkinter ( NeoViki_UI Format )

    Author: Viki (a) Vignesh Natarajan
'''

try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
    import tkinter.scrolledtext as scrolledtext
    import threading
    import tkFont
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialogs
    import Tkinter.scrolledtext as scrolledtext
    import tkFont
    import threading

from PIL import ImageTk, Image
from os import system
from platform import system as platform

class font:
    def __init__(self):
        self.size = 10
        self.name = 'consolas'
        self.bold = False
        self.italic = False

class color:
    def __init__(self):
        self.fg = 'black'
        self.bg = 'white'

class border:
    def __init__(self):
        self.color = 'black'
        self.thickness = 10

class UI_COMMON:
    def __init__(self):
        self.handle = None
        self.title="demo"
        self.color = color()
        self.border = border()
        self.font = font()
        self.width=200
        self.height=200

    def callback(self, func):
        self.handle.configure(command = func)

    def dimension(self, width, height):
        self.width = width
        self.height = height

    def disable(self):
        self.handle.configure(state='disabled')

    def enable(self):
        self.handle.configure(state='normal')

    def write(self, val):
        self.handle.configure(text=val)

    def read(self):
        #return self.handle.get('1.0', tk.END)
        return self.handle.get()

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.handle.configure(bg=self.color.bg)
        self.handle.configure(fg=self.color.fg)
        self.handle.configure(width=self.width)
        self.handle.configure(height=self.height)
        self.handle.config(font=(self.font.name, self.font.size))
        self.handle.place(x=self.x, y=self.y)


class WINDOW(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.resize = False
        self.title = ""
        self.handle = tk.Tk()
        self.width = self.handle.winfo_reqwidth()
        self.height = self.handle.winfo_reqheight()

    def gotoxy(self, x, y):
        #self.x=int(self.handle.winfo_screenwidth()/3 - self.width/2)
        #self.y=int(self.handle.winfo_screenheight()/3 - self.height/2)
        self.x = x
        self.y = y
        self.handle.winfo_toplevel().title(self.title)
        pos_n_dimension = str(self.width) + "x" + str(self.height)  + "+" + str(self.x) + "+" + str(self.y)
        self.handle.geometry(pos_n_dimension)
        self.handle.configure(bg=self.color.bg)
        if self.resize == True:
            self.handle.resizable(True, True)
        else:
            self.handle.resizable(False, False)

class button(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.handle = tk.Button(master=self.parent.handle,
                                image=self.pixelVirtual,
                                compound="c")
        self.handle.pack()


    def gotoxy(self, x, y):
        self.x = x
        self.y = y

        self.handle.configure(bg=self.color.bg)
        self.handle.configure(fg=self.color.fg)
        self.handle.configure(width=self.width)
        self.handle.configure(height=self.height)
        self.handle.config(font=(self.font.name, self.font.size))
        self.handle.place(x=self.x, y=self.y)

class input(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.handle = tk.Entry(self.parent.handle)
        self.handle.pack()

    def write(self, val):
        self.handle.insert(tk.END, val)

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.handle.configure(bg=self.color.bg)
        self.handle.configure(fg=self.color.fg)
        self.handle.configure(width=self.width)
        #self.handle.configure(height=self.height)
        self.handle.config(font=(self.font.name, self.font.size))
        self.handle.place(x=self.x, y=self.y)


class display_area(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.text_wrap = False
        self.handle = tk.scrolledtext.ScrolledText(master=self.parent.handle,
                                                   cursor="arrow",
                                                   undo=True)
        self.handle.pack()

    def write(self, val):
        self.handle.insert(tk.END, val)

    def read(self):
        return self.handle.get('1.0', tk.END)

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.handle.configure(bg=self.color.bg)
        self.handle.configure(fg=self.color.fg)
        self.handle.configure(width=self.width)
        self.handle.configure(height=self.height)

        if self.text_wrap == True:
            self.handle.config(wrap=tk.WORD)

        self.handle.config(font=(self.font.name, self.font.size))
        self.handle.place(x=self.x, y=self.y)

class label(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.color.bg = None
        self.handle = tk.Label(master=self.parent.handle, anchor="center", justify='center')
        self.handle.pack()

    def write(self, val):
        self.handle.config(text=val)

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.handle.configure(bg=self.color.bg)
        self.handle.configure(fg=self.color.fg)
        self.handle.configure(width=self.width)
        self.handle.configure(height=self.height)
        self.handle.config(font=(self.font.name, self.font.size))
        self.handle.place(x=self.x, y=self.y)


class logo(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.path = "/"
        self.image=None
        self.handle = tk.Label(self.parent.handle)
        self.handle.pack(expand=tk.YES, fill=tk.BOTH)
        self.value=""

    def write(self, value):
        self.handle.config(text=self.value)

    #Private Method
    def __import_image(self):
        _image = Image.open(self.path)
        _width, _height = _image.size
        _ratio = float(_height) / float(_width)
        self.height = int(float(self.width) * float(_ratio))

        if self.height == 0:
            self.height = 1

        _image.resize((self.width, self.height))
        self.image = ImageTk.PhotoImage(_image)

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.__import_image()
        self.handle.config(image=self.image)
        #self.handle.create_image(self.width, self.height, image=self.image, anchor=tk.NW)
        self.handle.configure(bg=self.color.bg)
        self.handle.configure(fg=self.color.fg)
        self.handle.configure(width=self.width)
        self.handle.configure(height=self.height)
        self.handle.config(font=(self.font.name, self.font.size))
        self.handle.place(x=self.x, y=self.y)


class progress_bar(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.speed=10
        self.handle = ttk.Progressbar(master=self.parent.handle, mode ='indeterminate')
        self.horizantal()
        self.handle.pack()

    def write(self, val):
        self.handle.config(text=val)

    def horizantal(self):
        self.handle.config(orient=tk.HORIZONTAL)

    def vertical(self):
        self.handle.config(orient=tk.VERTICAL)

    def update(self, val):
        self.handle['value'] = val

    def start(self):
        self.handle.start(self.speed)

    def stop(self):
        self.handle.stop()

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.handle.configure(length=self.width)
        s = ttk.Style()
        s.theme_use("default")
        s.configure("TProgressbar", thickness=self.height)
        self.handle.configure(style="TProgressbar")

        self.handle.place(x=self.x, y=self.y)

class box:
    def __init__(self, parent):
        self.parent = parent
        self.border = border()
        self.color = color()
        self.width = 10
        self.height = 10

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        w_mid = self.width/2
        h_mid = self.height/2

        self.handle = self.parent.handle.create_rectangle(self.x - self.width, self.y - self.height,
                                                          self.x + self.width, self.y + self.height,
                                                          width=self.border.thickness,
                                                          outline=self.border.color,
                                                          fill=self.color.fg )

'''
class line:
    def __init__(self, parent):
        self.parent = parent
        self.color = color()
        self.x1 = 1
        self.x2 = 1
        self.y1 = 2
        self.y2 = 2
        self.thickness = 2
        self.dashed = False

    def gotoxy(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        if self.dashed == False:
            self.handle = self.parent.handle.create_line( self.x1, self.y1,
                        self.x2, self.y2,
                        width=self.thickness,
                        fill=self.color.fg)
        else:
            self.handle = self.parent.handle.create_line( self.x1, self.y1,
                        self.x2, self.y2,
                        width=self.thickness,
                        fill=self.color.fg, dash=(4,4))
'''

class circle:
    def __init__(self, parent):
        self.parent = parent
        self.radius = 10
        self.border = border()
        self.color = color()

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.handle = self.parent.handle.create_oval(self.x - self.radius, self.y - self.radius,
                              self.x + self.radius, self.y + self.radius,
                                width=self.border.thickness,
                                outline=self.border.color,
                                fill=self.color.fg )

class text:
    def __init__(self, parent):
        self.parent = parent
        self.font = font()
        self.color = color()
        self.__font_attribute = ""
        self.__generate_font_attribute()
        self.value = ""

    def write(self, value):
        self.value = value

    #private method
    def __generate_font_attribute(self):
        self.__font_attribute = str(self.font.name) + " " + str(self.font.size)

        if self.font.italic == True:
            self.__font_attribute = self.__font_attribute + " " + "italic"

        if self.font.bold == True:
            self.__font_attribute = self.__font_attribute + " " + "bold"

    def gotoxy(self, x, y):
        self.x=x
        self.y=y
        self.__generate_font_attribute()
        self.handle = self.parent.handle.create_text(self.x, self.y,
                fill=self.color.fg, font=self.__font_attribute,
                text=self.value)

class canvas(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.handle = tk.Canvas(master=self.parent.handle)
        self.handle.pack()

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.handle.configure(bg=self.color.bg)
        self.handle.configure(width=self.width)
        self.handle.configure(height=self.height)
        self.handle.place(x=self.x, y=self.y)



def BEGIN():
    root = WINDOW()
    return root

def END(root):
    root.handle.attributes('-topmost',True)
    root.handle.focus_set()

    # Bring App to Front
    if platform() == 'Darwin':  # MacOS
        system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

    root.handle.lift()
    root.handle.mainloop()


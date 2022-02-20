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

class UI_COMMON:
    def __init__(self):
        self.handle = None
        self.var_title="demo"
        self.var_bg_color='#555'
        self.var_fg_color="black"
        self.var_border_color="black"
        self.var_width=200
        self.var_height=200
        self.var_dimension='' + str(self.var_width) + 'x' + str(self.var_height) + ''
        self.var_font_type='consolas'
        self.var_font_size='12'

    def dimension(self, w, h):
        self.var_width=w
        self.var_height=h
        self.handle.configure(width=self.var_width)
        self.handle.configure(height=self.var_height)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.handle.configure(bg=self.var_bg_color)

    def fg(self, fg_color):
        self.var_fg_color = fg_color
        self.handle.configure(fg=self.var_fg_color)

    def callback(self, func):
        self.handle.configure(command = func)

    def font(self, var_font_type):
        self.var_font_type = var_font_type
        self.handle.config(font=(self.var_font_type, self.var_font_size))

    def font_size(self, var_font_size):
        self.var_font_size = var_font_size
        self.handle.config(font=(self.var_font_type, self.var_font_size))

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
        self.handle.place(x=x, y=y)

class ROOT(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.handle = tk.Tk()
        self.bg(self.var_bg_color)
        self.title(self.var_title)
        self.dimension(self.var_width, self.var_height)
        self.disable_resize()

    def dimension(self, w, h):
        self.var_width = str(w)
        self.var_height = str(h)
        self.var_dimension = '' + str(self.var_width) + 'x' + str(self.var_height) + ''
        self.handle.geometry(self.var_dimension)
        w = self.handle.winfo_reqwidth()
        h = self.handle.winfo_reqheight()
        px=int(self.handle.winfo_screenwidth()/3 - w/2)
        py=int(self.handle.winfo_screenheight()/3 - h/2)
        self.handle.geometry('+{}+{}'.format(px, py))

    def disable_resize(self):
        self.handle.resizable(False, False)

    def enable_resize(self):
        self.handle.resizable(True, True)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.handle.configure(bg=self.var_bg_color)

    def title(self, title_string):
        self.var_title = title_string
        self.handle.winfo_toplevel().title(self.var_title)

    def gotoxy(self, x, y):
        self.handle.geometry('+{}+{}'.format(x, y))


class button(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.var_width=20
        self.var_height=5
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.handle = tk.Button(master=self.parent.handle,
                                image=self.pixelVirtual,
                                compound="c")
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.handle.pack()

    def dimension(self, w, h):
        self.var_width=w
        self.var_height=h
        self.handle.configure(width=self.var_width)
        self.handle.configure(height=self.var_height)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.handle.configure(bg=self.var_bg_color)


class input(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.var_width=10
        self.var_height=1
        self.handle = tk.Entry(self.parent.handle)
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.handle.pack()

    def dimension(self, w, h):
        self.var_width=w
        self.var_height=h
        self.handle.configure(width=self.var_width)
        #self.handle.configure(height=self.var_height)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.handle.configure(bg=self.var_bg_color)

    def write(self, val):
        self.handle.insert(tk.END, val)

class display_area(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.var_width=10
        self.var_height=10
        self.handle = tk.scrolledtext.ScrolledText(master=self.parent.handle,
                                                   cursor="arrow",
                                                   undo=True)
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.handle.pack()

    def enable_text_wrap(self):
        self.handle.config(wrap=tk.WORD)

    def write(self, val):
        self.handle.insert(tk.END, val)

    def read(self):
        return self.handle.get('1.0', tk.END)

class label(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.var_width=10
        self.var_height=1
        self.handle = tk.Label(master=self.parent.handle, anchor="center", justify='center')
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.handle.pack()

    def write(self, val):
        self.handle.config(text=val)


class logo(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.var_bg_color='white'
        self.parent=parent
        self.var_path = None
        self.image=None
        self.var_width=10
        self.var_height=10
        self.handle = tk.Label(self.parent.handle)
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.handle.pack(expand=tk.YES, fill=tk.BOTH)

    def write(self, val):
        self.handle.config(text=val)

    def import_image(self):
        _image = Image.open(self.var_path)
        _width, _height = _image.size
        _ratio = float(_height) / float(_width)
        self.var_height = int(float(self.var_width) * float(_ratio))

        if self.var_height == 0:
            self.var_height = 1

        _image.resize((self.var_width, self.var_height))
        self.image = ImageTk.PhotoImage(_image)
        self.dimension(self.var_width, self.var_height)

    def path(self, var_path):
        self.var_path=var_path
        self.import_image()
        self.handle.config(image=self.image)
        #self.handle.create_image(self.var_width, self.var_height, image=self.image, anchor=tk.NW)

class progress_bar(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.var_speed=10
        self.var_width=40
        self.var_height=1
        self.handle = ttk.Progressbar(master=self.parent.handle, mode ='indeterminate')
        self.dimension(self.var_width, self.var_height)
        self.horizantal()
        self.handle.pack()

    def speed(self, val):
        self.var_speed = val

    def write(self, val):
        self.handle.config(text=val)

    def horizantal(self):
        self.handle.config(orient=tk.HORIZONTAL)

    def vertical(self):
        self.handle.config(orient=tk.VERTICAL)

    def dimension(self, w, h):
        self.var_width=w
        self.var_height=h
        self.handle.configure(length=self.var_width)
        s = ttk.Style()
        s.theme_use("default")
        s.configure("TProgressbar", thickness=self.var_height)
        self.handle.configure(style="TProgressbar")

    def update(self, val):
        self.handle['value'] = val

    def start(self):
        self.handle.start(self.var_speed)

    def stop(self):
        self.handle.stop()

class text:
    def __init__(self, parent):
        self.parent = parent
        self.var_fg_color = 'black'
        self.var_font = "Times"
        self.var_size = 20
        self.var_bold = True
        self.var_italic = True
        self.var_font_attribute = ""
        self.__generate_font_attribute()
        self.value = ""
        self.x = 0
        self.y = 0

    def display(self, value):
        self.value = value

    def fg(self, fg_color):
        self.var_fg_color = fg_color

    def bg(self, bg_color):
        print "warning: text background cannot be set, set bg color in the canvas handle"

    def font(self, var_font):
        self.var_font = var_font

    def size(self, var_size):
        self.var_size = var_size

    def bold(self, flag):
        if flag == True:
            self.var_bold =  "bold"
        else:
            self.var_bold = ""

    def italic(self, flag):
        if flag == True:
            self.var_italic =  "italic"
        else:
            self.var_italic = ""

    #private method
    def __generate_font_attribute(self):
        self.var_font_attribute = str(self.var_font) + " " + str(self.var_size)

        if self.var_italic == True:
            self.var_font_attribute = self.var_font_attribute + " " + "italic"

        if self.var_bold == True:
            self.var_font_attribute = self.var_font_attribute + " " + "bold"

    def gotoxy(self, x, y):
        self.x=x
        self.y=y
        self.handle = self.parent.handle.create_text(self.x, self.y, fill=self.var_fg_color, font=self.var_font_attribute, text=self.value)

class canvas(UI_COMMON):
    def __init__(self, parent):
        UI_COMMON.__init__(self)
        self.parent=parent
        self.var_width=10
        self.var_height=10
        self.handle = tk.Canvas(master=self.parent.handle)
        self.dimension(self.var_width, self.var_height)
        self.bg(self.var_bg_color)
        #self.fg(self.var_fg_color)
        self.handle.pack()

def BEGIN():
    root = ROOT()
    return root

def END(root):
    root.handle.attributes('-topmost',True)
    root.handle.focus_set()

    # Bring App to Front
    if platform() == 'Darwin':  # MacOS
        system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

    root.handle.lift()
    root.handle.mainloop()


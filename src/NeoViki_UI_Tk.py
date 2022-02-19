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


class UI_COMMON:
    def __init__(self):
        self.object = None
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
        self.object.configure(width=self.var_width)
        self.object.configure(height=self.var_height)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.object.configure(bg=self.var_bg_color)

    def fg(self, fg_color):
        self.var_fg_color = fg_color
        self.object.configure(fg=self.var_fg_color)

    def gotoxy(self, x, y):
        self.object.place(x=x, y=y)

    def callback(self, func):
        self.object.configure(command = func)

    def font(self, var_font_type):
        self.var_font_type = var_font_type
        self.object.config(font=(self.var_font_type, self.var_font_size))

    def font_size(self, var_font_size):
        self.var_font_size = var_font_size
        self.object.config(font=(self.var_font_type, self.var_font_size))

    def disable(self):
        self.object.configure(state='disabled')

    def enable(self):
        self.object.configure(state='normal')

    def write(self, val):
        self.object.configure(text=val)

    def read(self):
        #return self.object.get('1.0', tk.END)
        return self.object.get()


class ROOT(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.object = tk.Tk()
        self.bg(self.var_bg_color)
        self.title(self.var_title)
        self.dimension(self.var_width, self.var_height)
        self.disable_resize()

    def dimension(self, w, h):
        self.var_width = str(w)
        self.var_height = str(h)
        self.var_dimension = '' + str(self.var_width) + 'x' + str(self.var_height) + ''
        self.object.geometry(self.var_dimension)
        w = self.object.winfo_reqwidth()
        h = self.object.winfo_reqheight()
        px=int(self.object.winfo_screenwidth()/3 - w/2)
        py=int(self.object.winfo_screenheight()/3 - h/2)
        self.object.geometry('+{}+{}'.format(px, py))

    def disable_resize(self):
        self.object.resizable(False, False)

    def enable_resize(self):
        self.object.resizable(True, True)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.object.configure(bg=self.var_bg_color)

    def title(self, title_string):
        self.var_title = title_string
        self.object.winfo_toplevel().title(self.var_title)

    def gotoxy(self, x, y):
        self.object.geometry('+{}+{}'.format(x, y))


class button(UI_COMMON):
    def __init__(self, root):
        UI_COMMON.__init__(self)
        self.root_handle=root.object
        self.var_width=20
        self.var_height=5
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.object = tk.Button(master=self.root_handle,
                                image=self.pixelVirtual,
                                compound="c")
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.object.pack()

    def dimension(self, w, h):
        self.var_width=w
        self.var_height=h
        self.object.configure(width=self.var_width)
        self.object.configure(height=self.var_height)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.object.configure(bg=self.var_bg_color)

class input(UI_COMMON):
    def __init__(self, root):
        UI_COMMON.__init__(self)
        self.root_handle=root.object
        self.var_width=10
        self.var_height=1
        self.object = tk.Entry(self.root_handle)
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.object.pack()

    def dimension(self, w, h):
        self.var_width=w
        self.var_height=h
        self.object.configure(width=self.var_width)
        #self.object.configure(height=self.var_height)

    def bg(self, bg_color):
        self.var_bg_color = bg_color
        self.object.configure(bg=self.var_bg_color)

    def write(self, val):
        self.object.insert(tk.END, val)


class display_area(UI_COMMON):
    def __init__(self, root):
        UI_COMMON.__init__(self)
        self.root_handle=root.object
        self.var_width=10
        self.var_height=10
        self.object = tk.scrolledtext.ScrolledText(master=self.root_handle,
                                                   cursor="arrow",
                                                   undo=True)
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.object.pack()

    def enable_text_wrap(self):
        self.object.config(wrap=tk.WORD)

    def write(self, val):
        self.object.insert(tk.END, val)

    def read(self):
        return self.object.get('1.0', tk.END)

class label(UI_COMMON):
    def __init__(self, root):
        UI_COMMON.__init__(self)
        self.root_handle=root.object
        self.var_width=10
        self.var_height=1
        self.object = tk.Label(master=self.root_handle, anchor="center", justify='center')
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.font(self.var_font_type)
        self.font_size(self.var_font_size)
        self.object.pack()

    def write(self, val):
        self.object.config(text=val)

class logo(UI_COMMON):
    def __init__(self, root):
        UI_COMMON.__init__(self)
        self.var_bg_color='white'
        self.root_handle=root.object
        self.var_path = None
        self.image=None
        self.var_width=10
        self.var_height=10
        self.object = tk.Label(self.root_handle)
        self.bg(self.var_bg_color)
        self.dimension(self.var_width, self.var_height)
        self.object.pack(expand=tk.YES, fill=tk.BOTH)

    def write(self, val):
        self.object.config(text=val)

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
        self.object.config(image=self.image)
        #self.object.create_image(self.var_width, self.var_height, image=self.image, anchor=tk.NW)


class progress_bar(UI_COMMON):
    def __init__(self, root):
        UI_COMMON.__init__(self)
        self.root_handle=root.object
        self.var_speed=10
        self.var_width=40
        self.var_height=1
        self.object = ttk.Progressbar(master=self.root_handle, mode ='indeterminate')
        self.dimension(self.var_width, self.var_height)
        self.horizantal()
        self.object.pack()

    def speed(self, val):
        self.var_speed = val

    def write(self, val):
        self.object.config(text=val)

    def horizantal(self):
        self.object.config(orient=tk.HORIZONTAL)

    def vertical(self):
        self.object.config(orient=tk.VERTICAL)

    def dimension(self, w, h):
        self.var_width=w
        self.var_height=h
        self.object.configure(length=self.var_width)
        s = ttk.Style()
        s.theme_use("default")
        s.configure("TProgressbar", thickness=self.var_height)
        self.object.configure(style="TProgressbar")

    def update(self, val):
        self.object['value'] = val

    def start(self):
        self.object.start(self.var_speed)

    def stop(self):
        self.object.stop()

def BEGIN():
    root = ROOT()
    return root

def END(root):
    root.object.mainloop()


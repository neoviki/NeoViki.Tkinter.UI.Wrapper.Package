'''
    Processing style UI api based on tkinter
    Author:
        Vignesh Natarajan (a) Viki
        https://vikiworks.io
'''

from tkinter import *
from tkinter import Scrollbar, Frame, Canvas
from os import system
from platform import system as platform

root    = Tk()

canvas  = None
color = 'black'
__fg = "black"
__bg = "white"
__outline_color = "black"
__fill_color    = "white"
__pos_x = 0
__pos_y = 0
__font_size = 12
__font_type = "Purisa"
__line_thickness      = 4
__border_thickness    = 4
__scrollbar_x = None
__scrollbar_y = None
frame = None

scroll_bar_buffer = 10000
__scroll_bar_enabled = False

def scrollbar_window_event_handler(window):
    global root, canvas, frame
    global __scrollbar_x, __scrollbar_y
    w, h = window.width, window.height
    canvas.config(  xscrollcommand = __scrollbar_x.set,
                    yscrollcommand = __scrollbar_y.set )
    canvas.configure(scrollregion = (0,0,w+scroll_bar_buffer,h+scroll_bar_buffer))
    print("event")

def scrollbar_window_event_listener():
    global root, canvas, frame
    root.bind("<Configure>", scrollbar_window_event_handler)

def window_event_handler(window):
    global root, canvas
    w, h = window.width, window.height
    canvas.config(width=w, height=h)
    print("event")

def window_event_listener():
    global root
    root.bind("<Configure>", window_event_handler)

def disable_window_resize():
    global root
    root.resizable(0, 0)
    root.update()

def window_width():
    global root
    return root.winfo_width()

def window_height():
    global root
    return root.winfo_height()

transparent = "" #color

def scrollbar_x():
    global canvas, frame, __scrollbar_x
    __scrollbar_x = Scrollbar(frame, orient=tkinter.HORIZONTAL)
    __scrollbar_x.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    __scrollbar_x.configure(command=canvas.xview)

def scrollbar_y():
    global canvas, frame, __scrollbar_y
    __scrollbar_y = Scrollbar(frame, orient=tkinter.VERTICAL)
    __scrollbar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    __scrollbar_y.configure(command=canvas.yview)

def create_canvas_with_scroll(width, height):
    global canvas, frame, root
    global __scroll_bar_enabled
    global __scrollbar_x, __scrollbar_y
    __scroll_bar_enabled = True
    frame = root
    canvas = Canvas(frame,
                        width=width, height=height,
                        bg=__fill_color, highlightthickness=0,
                        borderwidth=0, scrollregion=(0,0,width+scroll_bar_buffer,height+scroll_bar_buffer))

    scrollbar_x()
    scrollbar_y()

    canvas.config(  xscrollcommand = __scrollbar_x.set,
                    yscrollcommand = __scrollbar_y.set )
    canvas.pack(side=tkinter.LEFT,expand=True,fill=tkinter.BOTH)
    #canvas.grid()


def create_canvas(width, height):
    global canvas
    canvas = Canvas(root,
                        width=width, height=height,
                        bg=__fill_color, highlightthickness=0,
                        borderwidth=0)
    canvas.grid()

def circle(radius):
    global canvas
    return canvas.create_oval(__pos_x - radius, __pos_y - radius,
                              __pos_x + radius, __pos_y + radius,
                                width=__border_thickness,
                                outline=__outline_color,
                                fill=__fill_color )

def box(width, height):
    global canvas
    w_mid = width/2
    h_mid = height/2
    canvas.create_rectangle(__pos_x - w_mid, __pos_y - h_mid,
                            __pos_x + w_mid, __pos_y + h_mid,
                            fill=__fill_color,
                            outline = __outline_color,
                            width=__border_thickness)

def line(x1, y1, x2, y2):
    global canvas
    canvas.create_line( x1, y1,
                        x2, y2,
                        width=__line_thickness,
                        fill=__fill_color)

def dashed_line(x1, y1, x2, y2):
    global canvas
    canvas.create_line( x1, y1,
                        x2, y2,
                        width=__line_thickness,
                        fill=__fill_color,
                        dash=(4,4))

def fg_color(color):
    global __fg
    __fg = color

def bg_color(color):
    global __bg
    __bg = color

def outline(color):
    global __outline_color
    __outline_color = color

def fill(color):
    global __fill_color
    __fill_color = color


def gotoxy(x, y):
    global __pos_x, __pos_y
    __pos_x = x
    __pos_y = y

def text(text_string):
    global canvas
    canvas.create_text(__pos_x, __pos_y,
                        fill=__fill_color,
                        font = (__font_type, __font_size),
                        text=text_string)

def font_type(font_type):
    global __font_type
    __font_type = font_type

def font_size(font_size):
    global __font_size
    __font_size = font_size

def title(title_string):
    global root
    root.wm_title(title_string)

def focus_hack():
    if platform() == 'Darwin':  # How Mac OS X is identified by Python
        system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

def loop():
    global root
    if __scroll_bar_enabled == True:
        scrollbar_window_event_listener()
    else:
        window_event_listener()

    root.attributes('-topmost',True)
    root.focus_set()
    focus_hack()
    root.lift()

    root.mainloop()

def line_thickness(value):
    global __line_thickness
    __line_thickness = value

def border_thickness(value):
    global __border_thickness
    __border_thickness = value

def draw():
    title("shapes")
    fill("black")
    #create_canvas_with_scroll(500, 500)
    create_canvas(500, 500)
    print("R")
    outline("blue")
    fill("green")
    gotoxy(100,100)
    border_thickness(4)
    circle(20)
    fill(transparent)
    box(60,60)
    gotoxy(100,200)
    circle(20)
    gotoxy(200,400)
    line_thickness(4)
    dashed_line(100, 100, 200, 200)
    font_size(30)
    gotoxy(200,400)
    text("20")
    gotoxy(5000,400)
    box(60,60)
    loop()

draw()

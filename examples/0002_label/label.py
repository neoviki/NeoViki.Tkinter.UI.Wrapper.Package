import sys
sys.path.append('../../src')

from NeoViki_UI_Tk import *


def button_callback():
    print("hello")


root = BEGIN()
root.title = "demo"
root.width = 500
root.height = 500
#root.color.bg = '#555'
root.gotoxy(200,100)

obj = label(root)
obj.width = 30
obj.height = 5
obj.font.size = 12
obj.color.bg = 'green'
obj.color.fg = 'white'
obj.write("Line 1\n")
obj.write("Line 2\n")
obj.gotoxy(120, 100)
#obj.disable()
#obj.enable()

END(root)


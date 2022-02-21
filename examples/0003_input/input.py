import sys
sys.path.append('../../src')

from NeoViki_UI_Tk import *


def button_callback():
    print("hello")


root = BEGIN()
root.title = "demo"
root.width = 500
root.height = 500
#root.bg('#555')
root.gotoxy(200,100)

obj = input(root)
obj.width = 30
obj.height =  1
obj.font.size = 12
obj.color.bg = 'black'
obj.color.fg = "white"
obj.write("Input Box")
obj.gotoxy(120, 100)
#obj.disable()
#obj.enable()

END(root)


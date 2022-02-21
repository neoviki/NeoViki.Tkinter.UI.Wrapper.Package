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

obj = button(root)
obj.callback(button_callback)
obj.write("Button")
obj.width = 200
obj.height = 50

obj.font.size = 12
obj.color.bg = "blue"
obj.color.fg = "green"
obj.gotoxy(120, 100)
#obj.disable()
#obj.enable()

END(root)


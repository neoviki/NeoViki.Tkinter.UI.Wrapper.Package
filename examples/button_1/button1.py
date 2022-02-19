import sys
sys.path.append('../../src')
from NeoViki_UI_Tk import *

def button_callback():
    print("hello")


root = BEGIN()
root.title("demo")
root.dimension(500,500)
#root.bg('#555')
root.gotoxy(200,100)

obj = button(root)
obj.callback(button_callback)
obj.write("Button")
obj.dimension(200, 50)
obj.gotoxy(120, 100)
obj.font_size(12)
obj.bg('#111')
obj.fg("white")
#obj.disable()
#obj.enable()

END(root)


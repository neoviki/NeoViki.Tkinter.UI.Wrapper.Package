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

obj = display_area(root)
obj.dimension(30, 20)
obj.gotoxy(120, 100)
obj.font_size(12)
obj.bg('black')
obj.fg("white")
obj.write("Line 1\n")
obj.write("Line 2\n")

print(obj.read())
#obj.disable()
#obj.enable()

END(root)


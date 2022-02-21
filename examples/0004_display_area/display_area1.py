import sys
sys.path.append('../../src')

from NeoViki_UI_Tk import *

root = BEGIN()
root.title = "demo"
root.width = 500
root.height = 500
#root.bg('#555')
root.gotoxy(200,100)

obj = display_area(root)
obj.width = 30
obj.height= 20
obj.font.size = 12
obj.color.bg = 'black'
obj.color.fg = "white"
obj.write("Line 1\n")
obj.write("Line 2\n")
obj.gotoxy(120, 100)

print(obj.read())
#obj.disable()
#obj.enable()

END(root)


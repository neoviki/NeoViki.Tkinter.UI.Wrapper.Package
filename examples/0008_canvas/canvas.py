import sys
sys.path.append('../../src')
from NeoViki_UI_Python import *

root = BEGIN()
root.title = "demo"
root.dimension(500,500)
#root.color.bg = '#555'
root.gotoxy(200,100)

obj = canvas(root)
obj.dimension(200, 50)
obj.gotoxy(120, 100)

obj2 = text(obj)
obj2.write("test")
obj2.font.size = 20
obj2.color.fg = "green"
obj2.gotoxy(20,20)
#obj.disable()
#obj.enable()

END(root)


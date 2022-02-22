import sys
sys.path.append('../../src')
from NeoViki_UI_Python import *

root = BEGIN()
root.title = "demo"
root.dimension(500,500)
#root.bg('#555')
root.gotoxy(200,100)

obj = canvas(root)
obj.dimension(200, 50)
obj.gotoxy(120, 100)

obj2 = circle(obj)
obj2.color.fg = 'red'
obj2.gotoxy(20,20)

obj3 = box(obj)
obj3.width = 20
obj3.height = 40
obj3.border.thickness = 1
obj3.color.fg = 'blue'
obj3.color.bg = 'green'
obj3.gotoxy(60,60)

#obj4 = line(obj)
#obj4.thickness = 10
#obj4.color.fg = 'blue'
#obj4.gotoxy(10,200, 400, 200)


#obj.disable()
#obj.enable()

END(root)


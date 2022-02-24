import sys
sys.path.append('../../src')
from NeoViki_UI_Python import *

root = BEGIN()
root.title = "demo"
root.dimension(500,500)
#root.bg('#555')
root.gotoxy(200,100)

obj = canvas(root)
obj.dimension(500, 500)
obj.gotoxy(0, 0)

obj2 = circle(obj)
obj2.color.fg = 'red'
obj2.gotoxy(20,20)

obj3 = box(obj)
obj3.width = 20
obj3.height = 80
obj3.border.thickness = 1
obj3.color.fg = 'blue'
obj3.gotoxy(200,100)

obj3 = box(obj)
obj3.width = 20
obj3.height = 80
obj3.border.thickness = 1
obj3.color.fg = 'orange'
obj3.gotoxy(200,100)
#Rotate object by 30 degrees
obj3.rotate(30)


#obj4 = line(obj)
#obj4.thickness = 10
#obj4.color.fg = 'blue'
#obj4.gotoxy(10,200, 400, 200)


#obj.disable()
#obj.enable()

END(root)


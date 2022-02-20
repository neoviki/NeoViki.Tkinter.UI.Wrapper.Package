import sys
sys.path.append('../../src')
from NeoViki_UI_Tk import *

root = BEGIN()
root.title("demo")
root.dimension(500,500)
#root.bg('#555')
root.gotoxy(200,100)

obj = canvas(root)
obj.dimension(200, 50)
obj.gotoxy(120, 100)
obj2 = text(obj)
obj2.display("test")
obj2.size(12)
obj2.fg("white")
obj2.gotoxy(20,20)
#obj.disable()
#obj.enable()

END(root)


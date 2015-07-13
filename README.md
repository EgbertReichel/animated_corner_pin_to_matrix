# nuke_cornerpin_to_matrix
get animations from a cornerpin to a 4x4 matrix 

Additionally add those lines to your menu.py and your init.py files accordingly:

 - Entries to the init.py file to access this script in a python folder in the user .nuke directory.
 
nuke.pluginAddPath( './python' )

 - Entries to the menu.py file to access this script inside nuke from the menu.
 
import CornerPin_to_Matrix

m=nuke.menu('Nuke')
n=m.addMenu('Scripts')
n.addCommand('CornerPinToMatrix','CornerPin_to_Matrix.CP2MTX()',icon="CornerPin.png")

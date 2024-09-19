import maya.cmds as cmds
#List Selected
x = cmds.ls(sl=True)
#remove first index and give it a variable
y = x.pop(0)
#Get Shape Nodes from altered list
nurbsShapes = cmds.listRelatives(x, shapes=True)
#Parent the Curves to the transform
cmds.parent(x,y)
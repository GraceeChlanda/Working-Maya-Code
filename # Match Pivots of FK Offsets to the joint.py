#Match Pivots of FK Offsets to the joints
import maya.cmds as cmds
#List all Dag objects and dependency nodes in scene
selection = cmds.select(all=True)
list_of_Selection = cmds.list(selection)
print(list_of_Selection)
#Assign specific node type of selected to a variable

#Select the joint that shares the same position
#getAttr for both pivots
cmds.getAttr(ls.sl, "pivot")

#setAttr so offset matches JNT
---------------------------------------------------------
import maya.cmds as cmds
#list all joints in scene
joints = cmds.ls(type="joint")
#list all FK joints in the scene
for j in joints:
    FK_Joints = cmds.ls("*FK*")
    #print (FK_Joints)

#list all transform nodes in scene
offsets = cmds.ls(type="transform")
#list all offsest transforms in scene
for o in offsets:
    FK_Offsets = cmds.ls("*ffset*")
    print(FK_Offsets)

#find pivots
cmds.getAttr.FK_Joints(pivot.translate)

#Check one list iteration to another list iteration
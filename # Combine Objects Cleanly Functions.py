import maya.cmds as cmds

original_objects = cmds.ls(sl = True)

def combineSelected ():
    cmds.polyUnite(original_objects)
    cmds.rename('Combined_Mesh')
    return

def duplicate ():
    cmds.polyDuplicateAndConnect( "Combined_Mesh" )
    cmds.select(clear=True)
    return

def cleanUp():
    cmds.delete(original_objects,"Combined_Mesh")
    cmds.rename('Combined_Mesh1','Combined_Mesh')
    cmds.shadingNode('standardSurface1', asShader = True)
    cmds.select('Combined_Mesh')
    cmds.hyperShade(assign = 'standardSurface1')
    cmds.xform('Combined_Mesh', centerPivots = True)

if __name__ == "__main__":
    combineSelected()
    duplicate()
    cleanUp()
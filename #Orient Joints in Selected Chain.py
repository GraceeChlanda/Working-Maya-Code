import maya.cmds as cmds
#cmds.scriptEditorInfo(clearHistory=True)

#store joint list variables outside of the classes and functions

#Class: Prepare joint selection to modify
    #func: make list of selected "joints"
def listJoints():
    #select the hierarchy
    cmds.select(hierarchy=True)
    #make a list out of the selected joints
    unsortedJList = cmds.ls(type = "joint")
    #sort list bu pathname
    pathnameJList = sorted(cmds.ls(unsortedJList, long = True))
    #get the joint list sorted by pathname
    jList = cmds.ls(pathnameJList)
    
    #print(basenameJList)
    #print(jList)
    #print (type(basenameJList))
    return jList
    
    #func: create variable for all top joints
def getTopJoints():
    jList = listJoints()
    topJoints = jList[0]
    print(topJoints)
    return topJoints
    
def getBottomJoints():
    jList = listJoints()
    bottomJoints = jList[-1]
    print(bottomJoints)
    return bottomJoints
    
    #func: create variable for middle joints
def getMiddleJoints():
    jList = listJoints()
    middleJoints = jList[1:-1]
    print(middleJoints)
    return middleJoints
    
def getRootJoint():
    jList = listJoints()
    rootJoint = [root for root in jList if "oot" in root]
    print(rootJoint)
    return rootJoint
    #this returns a string in list and not an item i think
    
    #func: set translate of root joint to origin of scene, orient to world (o, 0, 0), set rotation axis to z,x,y
#def setRoot():
#    cmds.joint(rootJoint???)
        
def setRotOrder():
    jList = listJoints()
    for x in jList:
        cmds.joint(edit = True, rotationOrder = "yzx")
#orient everything but tip
def orientJoints():
    middleJoints = getMiddleJoints()
    for x in middleJoints:
        cmds.joint(edit = True, orientJoint = "zxy")

def queryJoint():
    jList = listJoints()
    refJoint = jList[-2]
    qJoint = cmds.joint(refJoint, query = True)
    return qJoint

def copyJoint():
    
    

#Query Joint before it in the heirarchy for its orient and edit the tip joints to copy that         
        





    #func: set translate of root joint to origin of scene, orient to world (o, 0, 0), set rotation axis to z,x,y
    def setRoot():
        cmds.joint(rootJoint???)
    #func: set joint radius to 1
    def setRadius():
        cmds.joint()
    #func: set orient of bottom joints
    def orientBottomJoints():
        cmds.joint(orient= 0,0,0???)
        
#Class Check for mistakes
    #Func: all joints should not have rotation transforms
    def checkTransformRotations():
        for x in lsHierarchy:
            if cmds.joint(rotation != 0???)
                cmds.error("A joint has transform rotations")
    #Func: Is the Root joint at the origin of the scene? (Translate 0,0,0)
    def checkRootPosition():
        if rootJoint != 0,0,0
            cmds.error("Move root joint to origin of the scene")
    #Func: are end joints set to an orient of 0, 0, 0?(world)
    def checkBottomJointOrient():
        for x in bottomJoints:
            if orient != 0,0,0
                cmds.error("Tip joint not oriented to world")
    
#Class make unbreakable
    #Func: Top joints in a chain split shouldn't have the ability to translate (lock them)
    #Func: Child joints should only be able to translate (stretch) down the bone axis
    #Func: lock joint radius
    #Func: Set preffered angle
    
 #Class mirror skeleton

 if __name__ == "__main__":
 


#store joint list variables outside of the classes and functions

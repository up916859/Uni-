import maya.cmds as cmds              
#function for editing an exsisting object
def userBox(*args):
    #Scale
    ys = cmds.intSliderGrp(yscale, q=True, v=True)
    xs = cmds.intSliderGrp(xscale, q=True, v=True)
    zs = cmds.intSliderGrp(zscale, q=True, v=True)
    #Move
    ym = cmds.intSliderGrp(ymove, q=True, v=True)
    xm = cmds.intSliderGrp(xmove, q=True, v=True)
    zm = cmds.intSliderGrp(zmove, q=True, v=True)
    #Rotate
    yr = cmds.intSliderGrp(yrotate, q=True, v=True)
    xr = cmds.intSliderGrp(xrotate, q=True, v=True)
    zr = cmds.intSliderGrp(zrotate, q=True, v=True)
    #Application
    cmds.polyCube(h = ys, w = xs, d = zs)
    cmds.move(y = ym, x = xm, z = zm)
    cmds.rotate(y = yr, x = xr, z = zr)
 
def userSphere(*args):
    rs = cmds.intSliderGrp(radiussphere, q=True, v=True)
    #Move
    yms = cmds.intSliderGrp(ymovesphere, q=True, v=True)
    xms = cmds.intSliderGrp(xmovesphere, q=True, v=True)
    zms = cmds.intSliderGrp(zmovesphere, q=True, v=True)
    #Rotate
    yrs = cmds.intSliderGrp(yrotatesphere, q=True, v=True)
    xrs = cmds.intSliderGrp(xrotatesphere, q=True, v=True)
    zrs = cmds.intSliderGrp(zrotatesphere, q=True, v=True)
    #Application
    cmds.polySphere(r= rs)
    cmds.move(y = yms, x = xms, z = zms)
    cmds.rotate(y = yrs, x = xrs, z = zrs)
#Creates cube window, toggles visability off
def cubeWindow(*args):
        cmds.showWindow("Cube")
        cmds.toggleWindowVisibility("Create_Geometirc_Primitive_Objects")
#Toggles cube window between visable
def cubeWinVis(*args):
        cmds.toggleWindowVisibility("Cube")
        cmds.toggleWindowVisibility("Create_Geometirc_Primitive_Objects")
#Creates sphere window, toggles visability off       
def sphereWindow(*args):
        cmds.showWindow("Sphere")
        cmds.toggleWindowVisibility("Create_Geometirc_Primitive_Objects")
#Toggles sphere window between visable
def sphereWinVis(*args):
        cmds.toggleWindowVisibility("Sphere")
        cmds.toggleWindowVisibility("Create_Geometirc_Primitive_Objects")
#Resets the scene
def resetScene(*args):
        cmds.file(new = True, f = True)
#Closes all windows with close window button
def exitMenu(*args):
        cmds.deleteUI("Cube")
        cmds.deleteUI("Sphere")
#Closes all windows with button
def exitMenuButton(*args):
        cmds.deleteUI("Cube")
        cmds.deleteUI("Sphere")
        cmds.deleteUI("Create_Geometirc_Primitive_Objects")
        
#Checks if main menu is already open, if so closes it    
if cmds.window("Create_Geometirc_Primitive_Objects", exists = True, q=True):
        cmds.deleteUI("Create_Geometirc_Primitive_Objects")
#Checks if sphere window is already open, if so closes it          
if cmds.window("Sphere", exists = True, q=True):
        cmds.deleteUI("Sphere")
#Checks if cube window is already open, if so closes it          
if cmds.window("Cube", exists = True, q=True):
        cmds.deleteUI("Cube")
        
cmds.scriptJob(cc=["SomethingSelected",selectObject])

def selectObject(*args):
    selections = cmds.ls(sl=True,long=True)
    selected = selections[0]
            
    
        

#Creates window and layout for main menu         
cmds.window("Create_Geometirc_Primitive_Objects", cc=exitMenu, ret=True)
cmds.columnLayout(nch = 4, rs=5, co=("both",5))
cmds.button("Cube", c=cubeWindow)
cmds.button("Sphere", c=sphereWindow)
cmds.button("Reset Scene", c=resetScene)
cmds.button("Exit", c=exitMenuButton)
cmds.showWindow("Create_Geometirc_Primitive_Objects")

#Create window and layput for cube creation           
cmds.window("Cube", h = 800, w = 400, cc=cubeWinVis, ret=True)
#Layout
cmds.rowColumnLayout(numberOfColumns = 1)
#Scale
yscale = cmds.intSliderGrp(f=True, label="Scale Y")
xscale = cmds.intSliderGrp(f=True, label="Scale X")
zscale = cmds.intSliderGrp(f=True, label="Scale Z")
#Move
ymove = cmds.intSliderGrp(f=True, label="Move Y")
xmove = cmds.intSliderGrp(f=True, label="Move X")
zmove = cmds.intSliderGrp(f=True, label="Move Z")
#Rotate
yrotate = cmds.intSliderGrp(f=True, label="Rotate Y")
xrotate = cmds.intSliderGrp(f=True, label="Rotate X")
zrotate = cmds.intSliderGrp(f=True, label="Rotate Z")
#Layout
cmds.rowColumnLayout(nc = 1)
cmds.button(label="Create Box", width=100, c=userBox)
#ScaleEdit
cmds.floatFieldGrp('scale', l= 'Scale', numberOfFields=3)
cmds.connectControl('scale', '%s.sy' % selected, index=2)
cmds.connectControl('scale', '%s.sx' % selected, index=3)
cmds.connectControl('scale', '%s.sz' % selected, index=4)
#MoveEdit
cmds.floatFieldGrp('move', l= 'Translate', numberOfFields=3)
cmds.connectControl('move', '%s.ty' % selected, index=2)
cmds.connectControl('move', '%s.tx' % selected, index=3)
cmds.connectControl('move', '%s.tz' % selected, index=4)
#RotateEdit
cmds.floatFieldGrp('rotate', l= 'Rotate', numberOfFields=3)
cmds.connectControl('rotate', '%s.ry' % selected, index=2)
cmds.connectControl('rotate', '%s.rx' % selected, index=3)
cmds.connectControl('rotate', '%s.rz' % selected, index=4)
#Return to the Main Menu
cmds.button(label="Main Menu", width=100, c=cubeWinVis)
#Close all windows
cmds.button("Exit", c=exitMenuButton)

#Create window and layput for cube creation           
cmds.window("Sphere", h = 800, w = 400, cc=sphereWinVis, ret=True)
#Layout
cmds.rowColumnLayout(numberOfColumns = 1)
#Scale
radiussphere = cmds.intSliderGrp(f=True, label="Radius")
#Move
ymovesphere = cmds.intSliderGrp(f=True, label="Move Y")
xmovesphere = cmds.intSliderGrp(f=True, label="Move X")
zmovesphere = cmds.intSliderGrp(f=True, label="Move Z")
#Rotate
yrotatesphere = cmds.intSliderGrp(f=True, label="Rotate Y")
xrotatesphere = cmds.intSliderGrp(f=True, label="Rotate X")
zrotatesphere = cmds.intSliderGrp(f=True, label="Rotate Z")

#Layout
cmds.rowColumnLayout(numberOfColumns=1)
cmds.button(label="Create Sphere", width=100, c=userSphere)
#ScaleEdit
cmds.floatFieldGrp('radius', l= 'Radius', numberOfFields=1)
cmds.connectControl('radius', '%s.sy' % selected, '%s.sx' % selected, '%s.sz' % selected, index=2)
cmds.floatFieldGrp('scale', l= 'Scale', numberOfFields=3)
cmds.connectControl('scale', '%s.sy' % selected, index=2)
cmds.connectControl('scale', '%s.sx' % selected, index=3)
cmds.connectControl('scale', '%s.sz' % selected, index=4)
#MoveEdit
cmds.floatFieldGrp('move', l= 'Translate', numberOfFields=3)
cmds.connectControl('move', '%s.ty' % selected, index=2)
cmds.connectControl('move', '%s.tx' % selected, index=3)
cmds.connectControl('move', '%s.tz' % selected, index=4)
#RotateEdit
cmds.floatFieldGrp('rotate', l= 'Rotate', numberOfFields=3)
cmds.connectControl('rotate', '%s.ry' % selected, index=2)
cmds.connectControl('rotate', '%s.rx' % selected, index=3)
cmds.connectControl('rotate', '%s.rz' % selected, index=4)
#Return to the Main Menu
cmds.button(label="Main Menu", width=100, c=sphereWinVis)
#Close all windows
cmds.button("Exit", c=exitMenuButton)

#http://help.autodesk.com/cloudhelp/2018/ENU/Maya-Tech-Docs/CommandsPython/
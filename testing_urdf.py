import pybullet as p
import time
import pybullet_data

p.connect(p.GUI) # connect to GUI

urdf_adress = pybullet_data.getDataPath() # get address of the urdf
p.setAdditionalSearchPath(urdf_adress) # set additional search path, having all urdf buildin
planeId = p.loadURDF("plane.urdf")
cutebox = p.loadURDF("cute_box.urdf",[0,0,1])

p.setGravity(0,0,-10)


for i in range(10000):
    time.sleep(0.01)
    p.stepSimulation()
    
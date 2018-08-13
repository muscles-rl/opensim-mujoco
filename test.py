import mujoco_py
from mujoco_py import load_model_from_path, MjSim, MjViewer
from mujoco_py.modder import TextureModder
import os
import random

model = mujoco_py.load_model_from_path("mujoco-rl/models/mujoco_gait9dof18musc.xml")
sim = mujoco_py.MjSim(model)
viewer = MjViewer(sim)
modder = TextureModder(sim)

t = 0

while True:
    # for name in sim.model.geom_names:
    #     modder.rand_all(name)
    #

#    sim.step()
    viewer.render()

    # # Clear muscles
    # for i in range(0,len(sim.data.ctrl)):
    #     sim.data.ctrl[i] = 0 #random.uniform(0, 1)

    # # TEST: Each two second extend and flex the ankle 
    # act = 0.05
    # if sim.data.time % 4.0 > 2:
    #     sim.data.ctrl[9] = act
    # else:
    #     sim.data.ctrl[10] = act

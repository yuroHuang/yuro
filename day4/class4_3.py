# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:55:20 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time  
x,y,z=mc.player.getTilePos()
for j in range(3):
    time.sleep(5)
    for i in range(5):
        r= random.randint(1,6)
        if r==1:
            mc.setBlocks(x,y,z,x+4,y,z,1)
            x=x+4
        elif r==2:
            mc.setBlocks(x,y,z,x-4,y,z,1)
            x=x-4
        elif r==3:
            mc.setBlocks(x,y,z,x,y,z+4,1)
            z=z+4
        elif r==4:
            mc.setBlocks(x,y,z,x,y,z-4,1)
            z=z-4
        elif r==5:
            mc.setBlocks(x,y,z,x,y+4,z,1)
            y=y+4
        else:
            mc.setBlocks(x,y,z,x,y-4,z,1)
            y=y-4
            
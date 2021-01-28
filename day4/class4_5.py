# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:15:40 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
import random
from time import sleep
mc=Minecraft.create()
myID=mc.getPlayerEntityId("Yoyocat")
mineral=[14,15,16,56,73,129,]
while True:
    sleep(0.5)
    r=random.choice(mineral)
    x,y,z=mc.entity.getTilePos(myID)
    mc.setBlocks(x+1,y,z+1,x-1,y+3,z-1,r)
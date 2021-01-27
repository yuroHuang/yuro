# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:17:51 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
import time
mcs=mc.create()

while True:
    x,y,z=mcs.player.getTilePos()
    mcs.postToChat("You are located on X:"+str(x)+\
                   ',Y:'+str(y)+",Z: "+str(z))
    time.sleep(0.5)
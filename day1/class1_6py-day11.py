# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:32:04 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mc
import time
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
i =0
while i < 5:
    mcs.player.setTilePos(x,y,z)
    time.sleep(2.5)
    y=y-10
    i=i+1
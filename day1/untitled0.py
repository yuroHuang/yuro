# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:32:22 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
print(mcs.player.getTilePos())
x=60
y=60
z=60
x=90
mcs.player.setTilePos(x,y,z)

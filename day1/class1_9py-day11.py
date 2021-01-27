# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:53:05 2021

@author: USERe
"
from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
mcs.setBlock(x+1,y,z,15)
mcs.setBlock(x+1,y,z+1,15)
mcs.setBlock(x+1,y,z-1,15)
mcs.setBlock(x,y,z+1,15)
mcs.setBlock(x,y,z-1,15)
mcs.setBlock(x-1,y,z-1,15)
mcs.setBlock(x-1,y,z,15)
mcs.setBlock(x-1,y,z+1,15)
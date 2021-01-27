# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:22:09 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
mc=Minecraft.create()
x,y,z=mc.player.getPos()
for i in range(40):
    mc.setBlock(x+i,y-i,z+i,1)
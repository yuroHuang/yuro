# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:37:03 2021

@author: USER
"""

from mcpi.minecraft import Minecraft 
mc=Minecraft.create()

while 1+1==2:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        mc.setBlock(x,y,z,20)
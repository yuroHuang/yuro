# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:33:12 2021

@author: USER
"""

from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    try:
        sh=int(input("Height :"))
        break
    except:
        print("That is not number")
h=(sh//2)+1
for i in range(h):
    x1=x+i
    y1=y+i
    z1=z+i
    x2=x+sh-i
    z2=z+sh-i
    mc.setBlocks(x1,y1,z1,x2,y,z2,24)
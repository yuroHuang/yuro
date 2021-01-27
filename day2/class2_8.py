# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:14:51 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
mcs.player.setTilePos(x,y,z,-19,63,-79)
mcs.setSign(x,y,z,68,0,"I love ","Python" ,"and"," Minecraft")
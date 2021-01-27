# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:55:33 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
mcs=mc.create()

while True:
    mcs.postToChat('hi')
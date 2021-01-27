# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:55:33 2021

@author: USER
"""

from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
userName=input('What\'s your name?')
massage=input("What\'s your massage?")
mcs.postToChat("[ "+userName+" ]"+massage)
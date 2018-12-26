# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:03:48 2018

@author: achem
"""


s = "azcbobobegghakl"
substring_length= 0
substring_increment = 1
character_place = 0

while character_place < len(s):
    if s[character_place] < s[character_place + substring_increment]:
        substring_increment += 1
    else:
        character_place += 1
        substring_increment = 1
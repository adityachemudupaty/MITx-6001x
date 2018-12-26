# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:41:47 2018

@author: achem
"""

s = 'bob'
current_place = 0
bob_counter = 0

while current_place < len(s):
    if current_place + 3 > len(s):
       
        break
    if s[current_place] == "b":
        if s[current_place + 1] == "o":
            if s[current_place + 2] == "b":
                bob_counter = bob_counter + 1
    current_place += 1
print(bob_counter)
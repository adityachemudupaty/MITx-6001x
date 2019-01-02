# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:03:48 2018

@author: achem
"""


s = "abcdeabc"
substring_length= 0
substring_increment = 0
character_place = 0
longest_length = 0
loop_increment = 0
string_length = len(s)

while character_place < string_length:
    if (character_place + substring_increment) > (string_length - 1):
        
    
    
    if s[(character_place + substring_increment)] < s[(character_place + substring_increment + 1)]:
        substring_increment += 1
        substring_length += 1
        
        
        if longest_length < substring_length:
            longest_length = substring_length
            print( s[character_place:character_place + substring_length] )
  
    
    else:
        character_place += 1
        substring_increment = 1
   
    
    print( s[character_place:(character_place + substring_length + 1)] )
    
    loop_increment += 1
    
    print(loop_increment)

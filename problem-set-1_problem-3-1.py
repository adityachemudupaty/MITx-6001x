# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 12:23:06 2018

@author: achem
"""

s = "zyxw"
substring_length= 0
substring_increment = 0
character_place = 0
longest_length = 0
loop_increment = 0
string_length = len(s)
beginning_char = 0
i = 0
while character_place < string_length:
    while (character_place + substring_increment) < (string_length - 1):
        
    
    
        if s[(character_place + substring_increment)] <= s[(character_place + substring_increment + 1)]:
            substring_increment = substring_increment + 1
            substring_length += 1
        
        
            if longest_length < substring_length:
                longest_length = substring_length
                beginning_char = character_place
                """print( s[character_place:character_place + substring_length + 1] )"""
        else:
            substring_length += 1
            
            break
        
    
    character_place += 1
    substring_increment = 0
    substring_length = 0
   
    
    
    
    loop_increment += 1
print( "Longest substring in alphabetical order is: " + s[beginning_char:(beginning_char + longest_length + 1)] )    
"""print(loop_increment)"""

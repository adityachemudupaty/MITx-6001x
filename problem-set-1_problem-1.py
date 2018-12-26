# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:06:27 2018

@author: achem

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
        Number of vowels: 5
"""
s = "psbeamaojc"
string_length = len(s)
number_vowels = 0
current_place = 0
while current_place < string_length:
    
    if s[current_place] == "a":
        number_vowels = number_vowels + 1
        current_place = current_place + 1
        
    elif s[current_place] == "e":
        number_vowels = number_vowels + 1
        current_place = current_place + 1
        
    elif s[current_place] == "i":
        number_vowels = number_vowels + 1
        current_place = current_place + 1
        
    elif s[current_place] == "o":
        number_vowels = number_vowels + 1
        current_place = current_place + 1
        
    elif s[current_place] == "u":
        number_vowels = number_vowels + 1
        current_place = current_place + 1
      
    else:
        current_place = current_place + 1
        
print("Number of vowels: " + str(number_vowels))
        
        
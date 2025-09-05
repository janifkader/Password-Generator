#Building the character pool

import string
#start with an character pool
char_pool = ''
#ask the user what they would like to include in their password
use_letters = input ("Include letters? (y/n):").strip().lower()== 'y'
use_digits = input ("Include digts? (y/n):").strip().lower()== 'y'
use_symbols = input ("Include symbols? (y/n):").strip().lower()== 'y'

#add to pool based on what the user chooses 
if use_letters:
    char_pool += string.ascii_letters # A-Z and a-z
if use_digits:
    char_pool += string.ascii_digits # 0-9
if use_symbols:
    char_pool += string.ascii_punctuation # Special Characters

    # Validate Selection (In order to validate have to pick one of each character)
if not char_pool:
print ("Error: You must select at least one type of character.") 
exit()
print("character pool created:"), char_pool 


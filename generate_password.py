# Problem Statement: 
# Write a Python program that prompts the user to enter his/her full name (without any spaces) and then 
# creates a secret password consisting of three letters (in lowercase) randomly picked up from his/her full name,
# and a random four-digit number. For example, if the user enters "JackClarusway", a secret password can probably
# be one of "jcs1578" or "yka8832" or "awu1250".

import random
import string

full_name = input("Please, enter your full name without space: ").lower()
num = string.digits
num2 = random.sample(num,4)
letters = random.sample(full_name,3)
all = letters + num2
password = ''.join(all)

print(password)

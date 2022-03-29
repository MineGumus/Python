# write a program that takes a string and checks if it contains consecutive vowels or not. 
# It should give Positive as an output if it contains consecutive vowels and Negative otherwise. 
# For example saetqi string contains a adjacent to e, which means that it contains consecutive vowels. 
# So it should give Positive as an output. On the other hand, if you take the string of statoqag, the output should be Negative.

string = input("Please, enter a string: ").lower()
vowel = 0
for i in string:
  if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    vowel = vowel+1
  else: 
    vowel = 0
  if vowel == 2:
    break
if vowel == 0:
  print("Negative")
else:
  print("Positive")

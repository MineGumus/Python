#Task:

# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(word):
    if word > word[0]:
      word = word[-1] + word[1:-1] + word[0]
      return word
    else:
      return word

# Task-1:
# Define a function to take a word and return negative meaning.
# Given a word, return a new word where "not " has been added to the front. 
# However, if the word already begins with "not", return the string unchanged.

def not_string(word):
    if word.strip()[0:4] == "not ":
        return word
    else:
        return "not " + word

"""
Write a function that accepts a string as an argument

The function should capitalize ONLY every other letter in the String

The function should then return the converted string

"""

#if changing string we need to initialize a new string as strings are immutable

def every_other_cap(word):
    changed_word = ""

    for i in range(len(word)):
        print(i)
        if i % 2 == 0:
            changed_word += word[i].upper()
        else:
            changed_word += word[i].lower()
    return changed_word
print(every_other_cap("heLLo there"))
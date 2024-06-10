# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

# The sorting should NOT be case sensitive

def sorter(textbooks):
    return sorted(textbooks,key=str.lower)

#* or casefold - makes string lower case as well. 3 args in sorted(iterable, key=decide the order, reverse=Boolean) could be len, str.func, 
def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)

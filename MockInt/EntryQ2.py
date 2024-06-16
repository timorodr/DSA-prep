"""
Write a function that accepts a string as an argument

The String is supposed to be HTML, but all the div elements are missing their closing tags (they have the < and >)

The functions job is to find and close all the divs in the provided HTML String

The function should retrun the entire corrected string
"""

# so we have the opening tags for the tags we have <div> but we also have <div>
# we have to check that every other div> we change it to /div>

def missing_tags(string):
    answer = ""
    closed_tag = ""
    substring = "<div>"

    div_count = string.count(substring)
    print(div_count)
    
    find_div = string.split()
    for div:
        if substring:
            find_div[i] += substring[:1] + "/" + substring[1:]
    print(find_div)
        # if div_count % 2 == 0:
        #     closed_tag += substring[:1] + "/" + substring[1:]

    
    return answer
        

print(missing_tags("the <div> on the street is missing the <div>"))
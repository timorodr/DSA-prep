# You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

# Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.

# Examples
# ["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
# ["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]

def tail_swap(strings):
    
    first_start = strings[0].split(":")[0]
    first_ends = strings[0].split(":")[1]
    second_start = strings[1].split(":")[0]
    second_ends = strings[1].split(":")[1]
    
    first_swap = first_start + ":" + second_ends
    second_swap = second_start + ":" + first_ends

    ans = [first_swap, second_swap]
    return ans
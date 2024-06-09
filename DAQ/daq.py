
file_content = """3 love
6 computers
2 dogs
4 cats
1 i
5 you"""



def decode(file_content):
    # Split the string content into lines
    lines = file_content.strip().split('\n')
    
    # Create a dictionary to map numbers to words
    num_to_word = {}
    for line in lines:
        number, word = line.strip().split()
        num_to_word[int(number)] = word
        print(num_to_word)

    # Determine the pyramid structure
    pyramid_end_indices = []
    n = 1
    total_numbers = 0
    while total_numbers + n <= len(num_to_word):
        total_numbers += n
        pyramid_end_indices.append(total_numbers)
        n += 1

    # Extract the relevant words
    decoded_words = [num_to_word[index] for index in pyramid_end_indices]

    # Form the decoded message
    decoded_message = ' '.join(decoded_words)
    return decoded_message

print(decode(file_content))
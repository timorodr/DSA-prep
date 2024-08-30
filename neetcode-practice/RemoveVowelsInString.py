class Solution:
    def removeVowels(self, s: str) -> str:
        letter_list = []

        vowel_dict = {vowel: True for vowel in 'aeiouAEIOU'}

        for letter in s:
            if not vowel_dict.get(letter, False):
                letter_list.append(letter)
            
        return "".join(letter_list)
string1 = "batbatbat"
string2 = "at"



class Solution:
    def stringInString(self, string1: str, string2: str) -> str:
        sub_len = len(string2)
        count = 0

        for i in range(len(string1)):
            if string1[i: i + sub_len] == string2:
                count+= 1
        return count
    

solution = Solution()
print(solution.stringInString(string1, string2))


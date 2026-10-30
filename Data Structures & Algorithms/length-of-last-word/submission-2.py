class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0 
        i = len(s) - 1
        
        
        while s[i] == ' ':
            i -= 1
         
        while i>= 0 and  s[i] != " ":
            length += 1
            i-= 1

        return length 

    

# return lenght of the last word in the string 
# string = non space

# brute: n / n --> strip and take the length of the last on e
# optimal: n / 1 --> start from back, skip spaces, while loop that goes until we reach a space or we reach the end of the string

# length
# loop reverse of s
    # while space: --> skip
    # while i >= 0 and curr is not a space --> length + 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while s[i] == " ":
            i -= 1
        
        while i>=0 and s[i] != " ":
            length+=1
            i -= 1
        return length
    


    

# return the len of the last word in the string 

# brute:
# optimal: 

# strip () --> grab last element from array --> grab len(last_element)

# n / 1

# length
# while if space --> skip
# while not space or reached sstart:
    # length += 1
#return lengts
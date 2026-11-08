class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n 
        seen = set()
        while curr != 1 and curr not in seen:
            seen.add(curr)
            curr = self.calculateNewCurr(curr)
        return curr ==1
    
    def calculateNewCurr(self, n):
        str_curr = str(n)
        summed = 0
        for curr in str_curr:
            num = int(curr)
            summed += num **2
        return summed




# checking if there is a cycle

# 1. square of a number's digits until 1 is reached
# stop when 1 is reached --> cycle (true)
# stop when a seen number is reached --> not a cycle (false)

# [1, 0, 0]
# 1 + 0 + 0 --> 1 (in a set)

# [1, 0, 1]

# logN, logN

# curr = n
# seen = set
# while curr != 1 or curr not in seen:
    # add curr to set
    # get new curr
# return n == 1

# calcualate new curr
# summed = 0
# for digit in str(n)
    # summed += digit**2
# return sum 

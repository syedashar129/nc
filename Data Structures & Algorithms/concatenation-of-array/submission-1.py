class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            res.append(num)
        for num in nums:
            res.append(num)
        return res

    
# create array of 2n
# show the same output twice

# brute: n / n --> 2 for loops and add into the array twice 
# optimal: 
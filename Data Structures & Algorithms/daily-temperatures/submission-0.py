class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (temperature, index) - order does not matter 
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append(temp, i)
        return res



# we are going to use monotomic decreasing stack
# we will add to stack and when we see a higher value, 
# we will check top of the stack and then keep popping and subtracting the indexes difference and storing it in the arra
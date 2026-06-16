class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                oldI = stack.pop()
                res[oldI] = i - oldI
            stack.append(i)

        return res


# look backwards
# monotonic decreasing stack --> looking back

# stack 
# res array

# loop thorugh the temperatures
#   while curr temperture > last temperture
#       pop the last one
#       res[last index] = curr index - last index
#    stack.append([i, temp])

# return res array
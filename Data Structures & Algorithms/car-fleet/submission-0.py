class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] # array of arrays
        pair.sort(reverse=True) #  reverse by position --> 
        
        stack = [] # stack of time arrivas

        for p, s in pair:
            time_arrived = (target - p) / s
            stack.append(time_arrived)

            if len(stack) > 1 and stack[-1] <= time_arrived:
                stack.pop()
            
        return len(stack)



# 2 arrays
# speed and position
# dest at target mi

# car can not pass a car ahead 
# fleet = same speed and smae position
# both reach destination is terminal point

# return # of fleets


#  1 , 2
#  4, 6
# 7, 10
# 10, 10

# 4, 1, 0, 7
# 6, 3, 1, 8
# 8, 5, 2, 9
# 10, 7, 3, 10
# 10, 9, 4, 10
# 10, 11, 5, 10

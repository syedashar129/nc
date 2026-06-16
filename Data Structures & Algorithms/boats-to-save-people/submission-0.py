class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        num_boats = 0

        while l < r:
            heavy = people[r]
            light = people[l]
            remaining_space = limit - heavy
            num_boats += 1
            r -= 1

            if remaining_space >= light:
                l += 1
        
        return num_boats


# sort 
# first pointer(l), second pointer (r)

# loop while l < r:
#   remain = limit - r
#   append final count 
#   decrease the r pointer

#   if lightest person (l) fit --> add and increase L 
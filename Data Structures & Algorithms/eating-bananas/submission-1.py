class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        speed = 0

        while lo <= hi:
            mid = (lo + hi) //2
            total_hours = self.get_hours(piles, mid, h)
            if total_hours > h:
                lo = mid + 1
            elif total_hours <= h:
                speed = mid
                hi = mid - 1
        
        return speed
    
    def get_hours(self, piles, mid, h):
        total_hours = 0 
        for pile in piles:
            total_hours += math.ceil(pile / mid)
        return total_hours

# minimum k per hour within h hours
# looking for efficint

# Method: binary search on answer 
    # based on max pile size

# lo = 1
# hi = max(piles)
# speed = 0

# while lo <= hi:
    # mid = (lo + hi) // 2
    # total_hours = test_speed(piles, mid, h)
     # binary search on new_speed 
        # here save the best result if less one 

# return speef

# test_speed(piles, mid, h)
    # total = 0
    # for pile in piles:
        # total += math.ceil(pile / mid)
    # return total 


# time: O(logn)
# space: O(1)
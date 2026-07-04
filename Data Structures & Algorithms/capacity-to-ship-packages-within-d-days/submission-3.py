class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        res = hi

        while lo <= hi:
            mid = (lo + hi) //2
            num_days = self.get_days(mid, weights)
            if num_days > days:
                lo = mid + 1
            else:
                res = mid
                hi = mid - 1
        
        return res


    def get_days(self, mid, weights):
        total_days = 1
        current_load = 0
        for weight in weights:
            if current_load + weight > mid:
                total_days += 1
                current_load = weight
            else:
                current_load += weight
        return total_days


# binary serach on max 
# max num of weights is key 

# lo = max(weights)
# hi = sum(weights)

# while lo <= hi
    # mid 
    # days = get_days(mid, weights, days)
    # binary search on days
        # * store the mid if <= than days

# get_days()
    # loop through weights and see how many days it takes for each day



# time: O(nlogm) 
# space: O(1)

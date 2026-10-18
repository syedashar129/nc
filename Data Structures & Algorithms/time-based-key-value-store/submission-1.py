from collections import defaultdict
class TimeMap:

    def __init__(self):
        #  Initializes the object of the data structure.
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #  Stores the key key with the value value at the given time timestamp.
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
        res = ""
        map_values = self.store.get(key, "")
        if not map_values:
            return res
        
        # [[happy, 1], [sad, 2]]
        lo, hi = 0, len(map_values) - 1
        # target = timsetamp 
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_val = map_values[mid][1] # 1, 2, etc
            if timestamp < mid_val:
                hi = mid - 1
            elif timestamp > mid_val:
                res = map_values[mid][0]
                lo = mid + 1
            else:
                return map_values[mid][0]
        return res

        
        
        



# alice : [happy, 1], [sad, 2]

# brute: n / mn
# optimal: logn / mn --> binary search fo rget 


        

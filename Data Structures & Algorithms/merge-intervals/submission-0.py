class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        for interval in intervals:
            if not res:
                res.append(interval)    
                continue 
            start = interval[0]
            end = interval[1]
            past_start = res[-1][0]
            past_end = res[-1][1]

            if start > past_end:
                res.append(interval)
            else:
                max_end = max(past_end, end)
                res.pop()
                res.append([past_start, max_end])
        return res


            

# return in any order 

# brute force: nlogn / n --> itertae intervals and sort them by the first number 
# optimal: 


# res = []
# sorted_intervals = sort the array
# loop inetrval in sorted_interval:
    # if the start > the max of the last --> append to res
    # if the start < the last --> take max of last second and current second + pop last + append(last first, curr max) to res
# return res
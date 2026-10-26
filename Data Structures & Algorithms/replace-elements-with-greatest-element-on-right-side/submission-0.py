class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1

        for i in range(len(arr) - 1, -1, -1):
            # store temp 
            tmp = arr[i]

            # set current as previous max 
            arr[i] = current_max

            # figure out new max 
            current_max = max(current_max, tmp)
            
        return arr



    
# replace last element with -1
# each element --> check all elements to the right and put it

# brute: n^2 / n --> for each element, loop and check what is the max by keeping track
# optimal: 

# loop backwards 
    # keep tr
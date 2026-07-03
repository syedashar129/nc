# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        
        while lo <= hi:
            mid = (hi + lo) // 2
            if guess(mid) == -1:
                hi = mid - 1
            elif guess(mid) == 1:
                lo = mid + 1
            else:
                return mid


# guess from 1 - n 
# guess weong --> high or lower --> binary search (guesss())
# ordered

# lo = 1
# hi = n

# while lo <= hi:
    # mid
    # if guess(mid) == -1 --> lo = mid + 1
    # elif guess(mid) == 1 --> hi = mid - 1
    # else (guess == 0) --> return mid



# time: O(logn)
# space: O(1)


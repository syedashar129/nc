class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0 
        hi = x
        res = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            prod_mid = mid * mid

            if prod_mid < x:
                res = mid 
                lo = mid + 1
            elif prod_mid > x:
                hi = mid - 1
            else:
                return mid 
        return res 

#  0 - n
# return sqrt(x) rounded down 
# no built in

# 9 --> 3 * 3
# 16 --> 4 * 4
# 25 --> 5 * 5

# get a number which can be multipleid by the same amount of times to get this number 
# 0 - 13
# 6 * 6 = 36
# 3 * 3 = 9 < 13 # lo = 0, mid = 3, hi = 6 

# lo = 0
# hi = x

# while lo <= hi:
    # mid 
    # prod_mid = mid * mid

    # if prod_mid < x:
        # res = mid
    # elif prod_mid > x;
    # else --> return mid

# return res 


# time: O(logn)
# space: O(1)

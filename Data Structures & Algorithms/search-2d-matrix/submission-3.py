class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.find_row(matrix, target)
        if row == -1: 
            return False
        else:
            return self.find_element_in_row(matrix, row, target)

    def find_row(self, matrix, target):
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid_row = (lo + hi) // 2
            first_element_in_row = matrix[mid_row][0]
            last_element_in_row = matrix[mid_row][-1]

            if first_element_in_row <= target <= last_element_in_row:
                return mid_row
            elif target > last_element_in_row:
                lo = mid_row + 1
            elif target < first_element_in_row:
                hi = mid_row - 1
        
        return -1

    def find_element_in_row(self, matrix, row, target):
        lo = 0 
        hi = len(matrix[row])

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_element = matrix[row][mid]
            if target < mid_element:
                hi = mid - 1
            elif target > mid_element:
                lo = mid + 1
            else:
                return True
        
        return False


    

# non-decreasing order
# sorted vertcally asc
# sorted horizoantally asc

# does exist? 

# high lvl sfind vertically, then find horizoantlly 
# check existence inside that mid row

# 2 methods 
# find row 
# find element in row 

# if no row found --> return false 
# if row found --> return element in row ()

# find row 
# binary search on vertical



# time: o(log(mn))
# O(1)
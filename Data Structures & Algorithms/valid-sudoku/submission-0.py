from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create sets
        col_set = defaultdict(set)
        col_set = defaultdict(set)

    
    # we need to check columns, row, squares
    # if present in any then --> return false since duplicate
    # iterate through each row, col by col

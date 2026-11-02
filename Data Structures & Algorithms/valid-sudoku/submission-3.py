class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue 
                if val in row_set[r] or val in col_set[c] or val in box_set[(r//3, c//3)]:
                    return False
                
                row_set[r].add(val)
                col_set[c].add(val)
                box_set[(r//3, c//3)].add(val)

        return True

    

# set for lookup 
# 3 things to check 
    # 1. row 
    # 2. column 
    # 3. box --> r // 3, c // 3

# checking if valid or not --> early return 
# skip . 
# go row ny row, column by column 

# n time 
# n space
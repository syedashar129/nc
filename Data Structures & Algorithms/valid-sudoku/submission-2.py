class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                if val in row_set[row] or val in col_set[col] or val in box_set[(row//3, col//3)]:
                    return False
                row_set[row].add(val)
                col_set[col].add(val)
                box_set[(row//3, col//3)].add(val)
        return True



    
# 1. row unique 
# 2. column uniqueness
# 3. box uniqeuness

# brute: n^3 / 1 
# optimal: 1 / 1 --> set with extistence check 

# row set, col set, box set 
# loop each row
    # loop each col
        # is [r][c] in col / row / box
            # yes --> False
            # no --> add [r][c] to each set 
# return True

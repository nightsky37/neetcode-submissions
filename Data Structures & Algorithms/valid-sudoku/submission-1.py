class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            table = set()
            for j in range(9):
                ch = board[i][j]
                if ch != '.':
                    if ch in table:
                        return False
                    table.add(ch)                        

        for i in range(9):
            table = set()
            for j in range(9):
                ch = board[j][i]
                if ch != '.':
                    if ch in table:
                        return False
                    table.add(ch)      
        
        center_idx_x_start = 1
        center_idx_y_start = 1
        for i in range(3):
            for j in range(3):
                table = set()
                for k in range(-1, 2, 1):
                    for l in range(-1, 2, 1):
                        ch = board[center_idx_x_start + 3 * i + k][center_idx_y_start + 3 * j + l]
                        if ch != '.':
                            if ch in table:
                                return False
                            table.add(ch)   
    
        return True

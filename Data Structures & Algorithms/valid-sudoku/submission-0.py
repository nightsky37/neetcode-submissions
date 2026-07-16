class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            table = {}
            for j in range(9):
                ch = board[i][j]
                if ch != '.':
                    table[ch] = table.get(ch, 0) + 1
                    if table[ch] > 1:
                        return False

        for i in range(9):
            table = {}
            for j in range(9):
                ch = board[j][i]
                if ch != '.':
                    table[ch] = table.get(ch, 0) + 1
                    if table[ch] > 1:
                        return False
        
        center_idx_x_start = 1
        center_idx_y_start = 1
        for i in range(3):
            for j in range(3):
                table = {}
                for k in range(-1, 2, 1):
                    for l in range(-1, 2, 1):
                        ch = board[center_idx_x_start + 3 * i + k][center_idx_y_start + 3 * j + l]
                        if ch != '.':
                            table[ch] = table.get(ch, 0) + 1
                            if table[ch] > 1:
                                return False
    
        return True

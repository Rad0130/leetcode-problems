class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            # Check if 'num' is not in the current row
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Check if 'num' is not in the current column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check if 'num' is not in the 3x3 sub-grid
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True
        
        def solve():
            # Iterate over every cell on the board
            for row in range(9):
                for col in range(9):
                    # If we find an empty cell, try to place a valid number
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):  # Try '1' to '9'
                            if is_valid(board, row, col, num):
                                # Place the number if it's valid
                                board[row][col] = num
                                
                                # Recursively try to solve the rest of the board
                                if solve():
                                    return True
                                
                                # If the current placement leads to no solution, backtrack
                                board[row][col] = '.'

                        return False  # No valid number can be placed, trigger backtracking

            return True  # Solved the board
        
        # Start solving the board
        solve()

# Example usage:
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

solver = Solution()
solver.solveSudoku(board)

# Output the solved board
for row in board:
    print(row)

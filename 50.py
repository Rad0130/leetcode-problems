class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # This will store all the solutions
        result = []
        
        # Initialize empty board
        board = [["." for _ in range(n)] for _ in range(n)]
        
        # Helper arrays to track attacks
        cols = [False] * n
        main_diag = [False] * (2 * n - 1)  # Tracks attacks on main diagonals
        anti_diag = [False] * (2 * n - 1)  # Tracks attacks on anti-diagonals
        
        # Backtracking function to place queens
        def backtrack(row):
            if row == n:
                # A valid configuration is found, convert the board to the required format
                result.append(["".join(board[i]) for i in range(n)])
                return
            
            # Try placing the queen in each column of the current row
            for col in range(n):
                if cols[col] or main_diag[row - col + n - 1] or anti_diag[row + col]:
                    continue  # This position is under attack, skip
                
                # Place the queen
                board[row][col] = 'Q'
                cols[col] = main_diag[row - col + n - 1] = anti_diag[row + col] = True
                
                # Move on to the next row
                backtrack(row + 1)
                
                # Backtrack, remove the queen
                board[row][col] = '.'
                cols[col] = main_diag[row - col + n - 1] = anti_diag[row + col] = False
        
        # Start backtracking from the first row
        backtrack(0)
        return result
        

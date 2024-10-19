class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Helper function to perform backtracking
        def backtrack(row, cols, diag1, diag2):
            # If we reach the last row, we found a valid solution
            if row == n:
                return 1

            count = 0
            for col in range(n):
                # Check if the current column or diagonals are attacked
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place the queen and mark the column and diagonals as occupied
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Recur to place queens in the next row
                count += backtrack(row + 1, cols, diag1, diag2)
                
                # Backtrack: remove the queen and unmark the column and diagonals
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            
            return count
        
        # Sets to track which columns and diagonals are occupied
        return backtrack(0, set(), set(), set())

# Testing the function
obj = Solution()
print(obj.totalNQueens(4))

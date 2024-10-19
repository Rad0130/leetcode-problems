class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Use sets to store seen numbers for rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                # Skip empty cells
                if board[i][j] == '.':
                    continue
                
                num = board[i][j]
                
                # Check row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                # Check column
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                # Check sub-box (calculate box index using integer division)
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        # If no issues, the board is valid
        return True
        

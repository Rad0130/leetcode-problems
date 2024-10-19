class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: if numRows is 1, return the input string
        if numRows == 1:
            return s
        
        # Initialize a list of empty strings for each row
        rows = [''] * min(numRows, len(s))
        
        # Variables to track the current row and direction
        cur_row = 0
        going_down = False
        
        # Traverse each character in the input string
        for char in s:
            # Add the character to the current row
            rows[cur_row] += char
            
            # Change direction when you reach the top or bottom
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
                
            # Move the current row pointer
            cur_row += 1 if going_down else -1
        
        # Combine all rows and return the result
        return ''.join(rows)

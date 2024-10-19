class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate over the characters in the string
        for char in s:
            if char in mapping:
                # Pop the top element from the stack if it's non-empty, else assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the stack's top element
                if mapping[char] != top_element:
                    return False
            else:
                # Push the opening bracket onto the stack
                stack.append(char)
        
        # If the stack is empty, return True, otherwise False
        return not stack

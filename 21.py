class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(curr_str, open_count, close_count):
            # Base case: If the current string is valid and complete
            if len(curr_str) == 2 * n:
                result.append(curr_str)
                return
            
            # Add an opening parenthesis if we haven't used all n opening ones
            if open_count < n:
                backtrack(curr_str + "(", open_count + 1, close_count)
            
            # Add a closing parenthesis if it doesn't exceed the number of opening ones
            if close_count < open_count:
                backtrack(curr_str + ")", open_count, close_count + 1)
        
        # Start the backtracking with an empty string and 0 open/close counts
        backtrack("", 0, 0)
        return result
        

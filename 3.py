class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize the stack with -1 to handle the edge case for the first valid substring
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of the '(' onto the stack
                stack.append(i)
            else:
                # Pop the top of the stack when we encounter a ')'
                stack.pop()

                if len(stack) == 0:
                    # If the stack is empty, push the current index onto the stack
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_length = max(max_length, i - stack[-1])

        return max_length

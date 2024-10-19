class Solution(object):
    def isMatch(self, s, p):
        # Create a DP table with size (len(s) + 1) x (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: Empty string matches with empty pattern
        dp[0][0] = True
        
        # Handle patterns with '*' that can match empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # If current characters match, inherit from dp[i-1][j-1]
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # * can either match zero or more of the preceding element
                    # Case 1: Match zero occurrences -> dp[i][j-2]
                    # Case 2: Match one or more occurrences -> dp[i-1][j]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]  # Match zero occurrences
        
        # The result will be in the bottom-right cell of the table
        return dp[len(s)][len(p)]

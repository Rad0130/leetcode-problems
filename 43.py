class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Lengths of the input string and pattern
        n, m = len(s), len(p)

        # Create the DP table
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Initialize the first row for patterns that start with '*'
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[n][m]
        

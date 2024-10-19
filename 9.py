class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last seen index of characters
        char_map = {}
        max_len = 0  # To store the maximum length of the substring
        start = 0  # Start index of the current window

        for i, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                # Move the start to the right of the last occurrence of the current character
                start = char_map[char] + 1
            # Update the latest index of the character
            char_map[char] = i
            # Calculate the max length
            max_len = max(max_len, i - start + 1)
        
        return max_len
        

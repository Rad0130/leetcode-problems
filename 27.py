class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If needle is an empty string, return 0
        if not needle:
            return 0
        
        # Get lengths of haystack and needle
        haystack_length = len(haystack)
        needle_length = len(needle)

        # Loop through haystack
        for i in range(haystack_length - needle_length + 1):
            # Check if the substring matches the needle
            if haystack[i:i + needle_length] == needle:
                return i  # Return the index if found
        
        return -1
        

class Solution(object):
    def minimumSteps(self, s):
        # To track how many 1's we've encountered
        one_count = 0
        # To track the minimum swaps needed
        min_steps = 0

        # Traverse the string from left to right
        for char in s:
            if char == '1':
                # Count how many 1's we have seen so far
                one_count += 1
            elif char == '0':
                # When we encounter a '0', we know it needs to swap with the previous '1's.
                # Each previous '1' needs to move past this '0'
                min_steps += one_count
        
        return min_steps

# Testing the function
obj = Solution()
s = "100"
print(obj.minimumSteps(s))

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0  # No jump needed if there's only one element

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # We don't need to jump from the last index
            farthest = max(farthest, i + nums[i])  # Update the farthest point we can reach
            
            if i == current_end:  # If we reach the end of the current jump
                jumps += 1  # We need to make a jump
                current_end = farthest  # Update the current_end to the farthest we can reach

                # Early exit if we can reach the end
                if current_end >= n - 1:
                    break

        return jumps
        

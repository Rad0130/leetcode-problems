class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Cyclic sort: place each number in its correct position (i.e., nums[i] = i+1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its target position (nums[nums[i] - 1])
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers are in their correct position, return n+1
        return n + 1
        

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: If the array is empty, return 0
        if not nums:
            return 0

        # Initialize the pointer for the next unique element
        i = 0

        # Iterate over the array starting from the second element
        for j in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[j] != nums[i]:
                i += 1  # Move to the next position
                nums[i] = nums[j]  # Place the unique element at the new position

        # The number of unique elements is i + 1 (index starts at 0)
        return i + 1
        

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # If we found a pivot
            # Step 2: Find the next larger element to swap with
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap the pivot with the next larger element
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])

# Testing the function
obj = Solution()
nums = [1, 2, 3]
obj.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
        

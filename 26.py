class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # Initialize the position pointer for non-val elements

        # Iterate over each element in the array
        for i in range(len(nums)):
            if nums[i] != val:  # If the current element is not equal to val
                nums[k] = nums[i]  # Place it at the k-th position
                k += 1  # Move the k pointer forward

        return k 

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Helper function to find the leftmost index of the target
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        # Helper function to find the rightmost index of the target
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)
        
        # Check if the target exists in the array
        if left_index <= right_index and left_index < len(nums) and nums[left_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]
        

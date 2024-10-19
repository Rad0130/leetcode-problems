class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # If target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left half
                else:
                    left = mid + 1  # Search right half
            else:
                # Right half must be sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Search right half
                else:
                    right = mid - 1  # Search left half
        
        return -1
        

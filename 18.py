class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sort the input array
        nums.sort()
        n = len(nums)
        res = []
        
        # First loop for the first element
        for i in range(n - 3):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Second loop for the second element
            for j in range(i + 1, n - 2):
                # Avoid duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Two-pointer approach for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # Move both pointers while avoiding duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
        

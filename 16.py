class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Step 1: Sort the array
        nums.sort()
        closest_sum = float('inf')  # Initialize with infinity
        
        # Step 2: Iterate through the array, using each number as the first element of the triplet
        for i in range(len(nums) - 2):
            # Step 3: Use two pointers to find the other two elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Step 4: Check if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Step 5: Adjust the pointers based on the current sum
                if current_sum < target:
                    left += 1  # Move the left pointer to the right to increase the sum
                elif current_sum > target:
                    right -= 1  # Move the right pointer to the left to decrease the sum
                else:
                    # If the current sum is exactly equal to the target, return the sum
                    return current_sum
        
        # Step 6: Return the closest sum after the loop
        return closest_sum
        

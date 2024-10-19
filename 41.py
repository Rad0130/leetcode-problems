class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:  # If the list is empty, return 0
            return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]  # Update max_left
                else:
                    water_trapped += max_left - height[left]  # Calculate trapped water
                left += 1  # Move the left pointer to the right
            else:
                if height[right] >= max_right:
                    max_right = height[right]  # Update max_right
                else:
                    water_trapped += max_right - height[right]  # Calculate trapped water
                right -= 1  # Move the right pointer to the left
        
        return water_trapped
        

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the width and height
            width = right - left
            h = min(height[left], height[right])
            # Calculate area
            area = width * h
            # Update maximum area
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            # If we've reached the end of the nums list, add the current permutation to results
            if start == len(nums):
                result.append(nums[:])  # Append a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next element in the list
                backtrack(start + 1)
                # Backtrack: undo the swap
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)  # Start the backtracking with the first index
        return result
        

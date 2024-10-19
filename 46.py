class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the numbers to handle duplicates
        nums.sort()
        result = []
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])  # Append a copy of the current permutation
                return
            
            for i in range(len(nums)):
                # Skip duplicates: if the current number is the same as the previous one and the previous one hasn't been used
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                
                # Choose the current number
                visited[i] = True
                path.append(nums[i])
                
                # Explore further
                backtrack(path)
                
                # Backtrack
                visited[i] = False
                path.pop()

        backtrack([])
        return result
        

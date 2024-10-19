class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(remaining_target, current_combination, start_index):
            # Base case: if the remaining target is 0, we found a valid combination
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            
            # Explore all candidates starting from 'start_index'
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # If the candidate exceeds the remaining target, skip it
                if candidate > remaining_target:
                    continue
                
                # Include the candidate in the current combination
                current_combination.append(candidate)
                
                # Since we can use the same candidate multiple times, pass 'i' instead of 'i+1'
                backtrack(remaining_target - candidate, current_combination, i)
                
                # Backtrack: remove the last added candidate
                current_combination.pop()
        
        # Start the backtracking with an empty combination and the full target
        backtrack(target, [], 0)
        
        return result
        

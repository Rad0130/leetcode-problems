class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, path, result):
            # Base case: if target is 0, we found a valid combination
            if target == 0:
                result.append(list(path))
                return
            # Explore further combinations
            for i in range(start, len(candidates)):
                # If the current candidate is the same as the previous one, skip to avoid duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the candidate exceeds the target, no point in continuing
                if candidates[i] > target:
                    break
                # Otherwise, include the candidate and recurse
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path, result)
                # Backtrack and remove the last element from the path
                path.pop()

        # Sort the candidates to help manage duplicates
        candidates.sort()
        result = []
        backtrack(0, target, [], result)
        return result
        

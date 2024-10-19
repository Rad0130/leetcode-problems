class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to letters according to telephone buttons
        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Backtracking function to generate combinations
        def backtrack(index, path):
            # If the path length is equal to digits length, we have a complete combination
            if index == len(digits):
                combinations.append(path)
                return
            
            # Get the characters that the current digit maps to, and loop through them
            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                # Append the current letter and move to the next digit
                backtrack(index + 1, path + letter)
        
        # Result list to store the combinations
        combinations = []
        backtrack(0, "")
        return combinations
        

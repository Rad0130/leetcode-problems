class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        # Recursive call to get the previous term in the sequence
        previous_term = self.countAndSay(n - 1)
        
        # Initialize an empty string to store the current result
        result = ""
        
        # Process the previous term with run-length encoding
        count = 1
        for i in range(1, len(previous_term)):
            if previous_term[i] == previous_term[i - 1]:
                # Increment count if the current digit is the same as the previous one
                count += 1
            else:
                # Append the count followed by the previous digit to the result
                result += str(count) + previous_term[i - 1]
                # Reset count for the new digit
                count = 1
        
        # Append the last counted group to the result
        result += str(count) + previous_term[-1]
        
        return result
        

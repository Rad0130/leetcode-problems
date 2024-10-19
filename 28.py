class Solution(object):
    def divide(self, dividend, divisor):
        # Define the limits for 32-bit signed integers
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # This is to find how many times the divisor can fit into the dividend
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Double the divisor until it's greater than the dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest found multiple of divisor from dividend
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the quotient
        if negative:
            quotient = -quotient
        
        # Return the quotient limited to 32-bit signed integer range
        return max(INT_MIN, min(quotient, INT_MAX))
        

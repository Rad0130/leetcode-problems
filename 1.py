class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Helper function to find the kth bit in Sn
        def find_bit(n, k):
            # Base case: S1 is "0", so if n == 1, return "0"
            if n == 1:
                return '0'
            
            mid = (2 ** (n - 1))  # Middle index in Sn

            if k == mid:
                return '1'  # Middle element is always "1"
            elif k < mid:
                return find_bit(n - 1, k)  # Left part is the same as Sn-1
            else:
                # Right part corresponds to reverse(invert(Sn-1)), invert the bit
                # Transform k to the corresponding index in Sn-1
                corresponding_k = 2 ** n - k
                return '0' if find_bit(n - 1, corresponding_k) == '1' else '1'

        return find_bit(n, k)

# Example usage:
obj = Solution()
n = 4
k = 11
print(obj.findKthBit(n, k))  # Output: "1"

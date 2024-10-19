class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Mapping of integers to their corresponding Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_num = ""
        
        # Loop through the values and build the Roman numeral
        for i in range(len(val)):
            # While the current value can be subtracted from num
            while num >= val[i]:
                roman_num += syms[i]  # Append the corresponding symbol
                num -= val[i]         # Subtract the value from num
        
        return roman_num
        

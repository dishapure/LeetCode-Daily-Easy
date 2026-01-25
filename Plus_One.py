class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Convert digits to string
        string = ""
        for i in range(len(digits)):
            string += str(digits[i])
        
        # Convert to int and add 1
        var = int(string) + 1
        
        # Convert back to list of digits
        nnum = []
        for i in str(var):
            nnum.append(int(i))  # convert each character back to int
        
        return nnum

# Example usage
sol = Solution()
num = [1, 2, 3]
print(sol.plusOne(num))  # Output: [1, 2, 4]

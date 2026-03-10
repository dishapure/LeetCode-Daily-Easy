class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        letters = []

        for c in s:
            if c.isalpha():
                letters.append(c)

        letters = letters[::-1]

        res = ""
        i = 0

        for c in s:
            if c.isalpha():
                res += letters[i]
                i += 1
            else:
                res += c

        return res

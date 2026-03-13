class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
                """
        res = ""

        for i in range(k-1,-1,-1):
            res += s[i]
            
        return res+s[k:]

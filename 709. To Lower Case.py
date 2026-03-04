class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for ch in s:
            if ch.isupper():
                res.append(ch.lower())
            else:
                res.append(ch)

        return ''.join(res)

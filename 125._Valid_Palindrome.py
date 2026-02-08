class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())

        arr = []
        arr2 = []

        for i in range(len(s)):
            arr.append(s[i])

        for j in range(len(s) - 1, -1, -1):
            arr2.append(s[j])

        if arr == arr2:
            return True
        else:
            return False

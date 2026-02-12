class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        sus = []
        for i in range(len(s)):
            sus.append(s[i])

        for i in range(len(s)):
            count_of_s = sus.count(s[i])
            if count_of_s == 1:
                return sus.index(s[i])
                break
        else:
            return -1
           

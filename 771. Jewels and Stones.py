class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        res = 0

        for ch in stones:
            if ch in jewels:
                res +=1

        return res

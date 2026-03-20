class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) > len(t):
            lens = len(s)
        else:
            lens = len(t)
            
        sc1 = sorted(s)
        sc2 = sorted(t)

        #print(sc1,sc2)
        res = []
        for i in range(lens):
            for ch in sc2:
                if ch in sc1:
                    sc1.remove(ch)
                else:
                    res.append(ch)

        return res[0]

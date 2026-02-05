class Solution(object):
    def hammingWeight(self, n):
        nn = bin(n)
        wbin = nn[2:]
        count = 0

        for i in range(len(wbin)):
            if wbin[i] == '1':
                count += 1

        return count

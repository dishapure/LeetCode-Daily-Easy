class Solution:
    def maxPower(self, s):
        max_power = 1
        curr = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                curr = 1
            max_power = max(max_power, curr)

        return max_power

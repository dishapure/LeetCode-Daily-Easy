class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
                """

        A = 0
        late_streak = 0

        for ch in s:
            if ch == 'A':
                A += 1
                late_streak = 0
            elif ch == 'L':
                late_streak += 1
                if late_streak == 3:
                    return False
                    break
            else:  # 'P'
                late_streak = 0
        else:
            if A < 2:
                return True
            else:
                return False

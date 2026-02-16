class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
                """
        magazine = list(magazine)

        res = ""
        mgi = []

        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                res = res + ransomNote[i]
                magazine.remove(ransomNote[i])  

        if res == ransomNote:
            return True
        else:
            return False

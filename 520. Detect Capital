class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        elementOne = word[0]
        if word.isupper() == True:
            return True
        elif word.islower() == True:
            return True
        elif elementOne.isupper() and word[1:].islower():
            return True
        else:
            return False
        

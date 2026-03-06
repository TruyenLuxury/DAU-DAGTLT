class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = 0
        length = len(s) - 1
        while length >= 0 and s[length] == " ":
            length -= 1
        while length >= 0 and s[length] != " ":
            d += 1
            length -= 1
        return d
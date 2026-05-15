class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = {}
        for c in s:
            counts[c] = counts.get(c,0) + 1
        for c in t:
            counts[c] = counts.get(c,0) - 1
            if counts[c] < 0:
                return c
        return ""
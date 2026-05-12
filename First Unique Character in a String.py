class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for i in s:
            counts[i] = counts.get(i,0) + 1
        for d,i in enumerate(s):
            if counts[i] == 1:
                return d
        return -1
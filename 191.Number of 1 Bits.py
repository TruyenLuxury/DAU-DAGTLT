class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        dem = 0
        while (n):
            dem += n & 1
            n >>= 1
        return dem
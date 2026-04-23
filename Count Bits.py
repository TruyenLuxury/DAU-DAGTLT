class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)
        for i in range(1,n+1):
            ans[i] = ans[i >> 1] + ( i & 1 ) # Nếu i là số chẵn thì số bit 1 của nó bằng số bit 1 của i >> 1, nếu i là số lẻ thì số bit 1 của nó bằng số bit 1 của i >> 1 + 1
        return ans
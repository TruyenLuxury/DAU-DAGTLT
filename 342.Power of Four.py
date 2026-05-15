class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 4 == 0: 
            n //= 4 # Nếu n là bội của 4 thì ta chia n cho 4, nếu n không phải là bội của 4 thì ta dừng vòng lặp
        return n == 1
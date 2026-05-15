class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1          # Lấy bit cuối cùng
        n >>= 1               # Dịch phải 1 bit
        while n:
            curr = n & 1      # Lấy bit hiện tại
            if curr == prev:  # Nếu 2 bit liền kề giống nhau → False
                return False
            prev = curr
            n >>= 1
        return True
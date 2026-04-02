class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        dem = 0
        while (n):
            dem += n & 1 # Tăng biến đếm nếu bit cuối cùng của n là 1
            n >>= 1 # Dịch n sang phải 1 bit để kiểm tra bit tiếp theo
        return dem
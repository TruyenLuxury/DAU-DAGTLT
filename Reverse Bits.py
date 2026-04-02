class Solution(object):
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result <<= 1          # dịch trái để tạo chỗ
            result |= (n & 1)     # lấy bit cuối của n
            n >>= 1              # dịch phải n  
        return result
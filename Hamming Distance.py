class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        count = 0
        while xor:
            count += xor & 1 # Kiểm tra bit cuối cùng của xor, nếu nó là 1 thì tăng count lên 1
            xor >>= 1 # Dịch bit của xor sang phải để kiểm tra bit tiếp theo
        return count
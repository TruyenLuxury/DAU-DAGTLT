class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1
        while mask < num:
            mask = (mask << 1) | 1 # Tạo một mask có tất cả các bit bên dưới bit cao nhất của num được đặt thành 1
        return num ^ mask 
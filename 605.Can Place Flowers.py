class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        size = len(flowerbed)
        for i in range(size):
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)# Kiểm tra xem vị trí bên trái có trống hay không. Nếu i là 0 (vị trí đầu tiên) hoặc nếu phần tử bên trái (flowerbed[i - 1]) bằng 0, thì left_empty sẽ được đặt thành True.
            right_empty = (i == size - 1) or (flowerbed[i + 1] == 0)# Kiểm tra xem vị trí bên phải có trống hay không. Nếu i là size - 1 (vị trí cuối cùng) hoặc nếu phần tử bên phải (flowerbed[i + 1]) bằng 0, thì right_empty sẽ được đặt thành True.
            if flowerbed[i] == 0 and left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return n <= 0
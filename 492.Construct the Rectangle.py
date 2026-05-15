class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(area ** 0.5) # Bắt đầu với chiều rộng w là căn bậc hai của diện tích, vì chúng ta muốn tìm cặp số gần nhau nhất
        while area % w != 0: # Kiểm tra nếu area không chia hết cho w, nếu không thì giảm w đi 1 và kiểm tra lại
            w -= 1
        return [area // w, w]
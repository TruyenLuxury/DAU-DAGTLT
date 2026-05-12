class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        min_row = m
        min_col = n
        for a, b in ops:# Duyệt qua danh sách các phép toán trong ops và cập nhật min_row và min_col bằng cách lấy giá trị nhỏ nhất giữa min_row và a, cũng như min_col và b. Điều này sẽ giúp xác định kích thước của vùng được tăng lên bởi tất cả các phép toán.
            min_row = min(min_row, a)
            min_col = min(min_col, b)
        return min_row * min_col
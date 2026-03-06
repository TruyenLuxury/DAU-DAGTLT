class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)# Mỗi hàng của tam giác Pascal bắt đầu và kết thúc bằng 1, do đó chúng ta khởi tạo một hàng mới với tất cả phần tử là 1.
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]# Mỗi phần tử trong hàng hiện tại (ngoại trừ phần tử đầu tiên và phần tử cuối cùng) được tính bằng cách lấy tổng của hai phần tử ở hàng trước đó, cụ thể là phần tử ngay trên nó (triangle[i-1][j]) và phần tử ngay trên nó nhưng lệch sang trái (triangle[i-1][j-1]).
            triangle.append(row)
        return triangle
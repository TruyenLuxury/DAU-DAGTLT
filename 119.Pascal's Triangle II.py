class Solution:
    def getRow(self, rowIndex):
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Cập nhật từ phải sang trái để tránh dùng giá trị đã sửa
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
            row.append(1)
        
        return row
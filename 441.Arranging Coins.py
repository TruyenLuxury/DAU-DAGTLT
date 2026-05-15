class Solution:
    def arrangeCoins(self, n): # Số lượng hàng tối đa có thể được xếp đầy đủ với n đồng xu
        row = 1
        while n >= row:
            n -= row
            row += 1
        return row - 1
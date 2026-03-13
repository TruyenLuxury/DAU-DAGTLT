class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res =""
        while columnNumber:
            columnNumber -= 1
            remainder = columnNumber % 26 # Tính phần dư để xác định chữ cái tương ứng (0-25)
            res = chr(columnNumber % 26 + 65) + res # Chuyển phần dư thành chữ cái (A-Z) và thêm vào kết quả
            columnNumber //= 26 # Chia columnNumber cho 26 để tiếp tục xử lý phần còn lại
        return res
class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for char in columnTitle:
            result = result * 26 +(ord(char)-ord('A')+1)# Tính giá trị số tương ứng với chữ cái (A=1, B=2, ..., Z=26) và cộng vào kết quả
        return result
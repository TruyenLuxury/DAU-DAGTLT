class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]# Trả về chuỗi nhị phân của tổng hai số nhị phân a và b. Hàm int(a, 2) chuyển đổi chuỗi a từ hệ nhị phân sang số nguyên, tương tự với b. Sau đó, hàm bin() chuyển đổi tổng của hai số nguyên trở lại chuỗi nhị phân, và [2:] loại bỏ phần '0b' ở đầu chuỗi kết quả.
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        total = 1
        for i in range(2, int(num ** 0.5) + 1):# Duyệt qua các số từ 2 đến căn bậc hai của num để tìm các ước số
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total == num # Kiểm tra nếu tổng các ước số bằng num, nếu có thì num là một số hoàn hảo và trả về True, ngược lại trả về FalseS
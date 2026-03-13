class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):# Duyệt mảng digits từ cuối về đầu để thực hiện phép cộng 1.
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        z = y[::-1] # Đảo ngược chuỗi

        if y == z:  # So sánh chuỗi ban đầu và chuỗi đảo ngược
            return True
        else:
            return False
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():# Nếu ký tự tại vị trí left không phải là chữ cái hoặc số, thì tăng left lên 1 để bỏ qua ký tự đó.
                left += 1
            while left < right and not s[right].isalnum():# Nếu ký tự tại vị trí right không phải là chữ cái hoặc số, thì giảm right xuống 1 để bỏ qua ký tự đó.
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
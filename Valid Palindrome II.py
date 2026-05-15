class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(s):
            return s == s[::-1]
        if is_palindrome(s):
            return True
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                b1 = is_palindrome(s[:l]+s[l+1:])
                b2 = is_palindrome(s[:r]+s[r+1:])
                return b1 or b2
            l += 1
            r -= 1
        return True
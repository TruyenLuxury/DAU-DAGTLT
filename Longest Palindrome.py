class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sdict = {}
        odd = 0
        count = 0
        for i in s:
            if i in sdict:# Đếm tần suất của mỗi ký tự trong chuỗi bằng cách sử dụng một dictionary
                sdict[i] += 1
            else:
                sdict[i] = 1
        for i in sdict.keys():# Duyệt qua các ký tự và tần suất của chúng trong chuỗi
            freq = sdict[i]
            if freq % 2 == 0:
                count += freq
            else:# Nếu tần suất là lẻ, chúng ta có thể sử dụng tất cả các ký tự đó trừ đi một ký tự để tạo thành một phần của chuỗi palindrome. Chúng ta cũng đánh dấu rằng chúng ta đã gặp một ký tự có tần suất lẻ để có thể thêm một ký tự vào giữa chuỗi palindrome sau này.
                count += freq - 1
                odd += 1
        if odd:
            count += 1
        return count
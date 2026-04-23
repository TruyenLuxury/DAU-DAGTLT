class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)
        left , right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vowels: # Nếu s[left] không phải là nguyên âm thì ta tăng left lên 1, nếu s[left] là nguyên âm thì ta dừng vòng lặp
                left += 1
            while left < right and s[right] not in vowels: # Nếu s[right] không phải là nguyên âm thì ta giảm right xuống 1, nếu s[right] là nguyên âm thì ta dừng vòng lặp
                right -= 1
            s[left], s[right] = s[right], s[left] # Nếu s[left] và s[right] đều là nguyên âm thì ta hoán đổi chúng với nhau
            left += 1 
            right -= 1
        return "".join(s) # Cuối cùng ta trả về chuỗi sau khi đã hoán đổi nguyên âm với nhau, ta sử dụng join để nối các phần tử trong list s thành một chuỗi mới và trả về kết quả đó.
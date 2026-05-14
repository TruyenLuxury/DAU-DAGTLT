class Solution:
    def countSegments(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):# Kiểm tra nếu ký tự hiện tại không phải là khoảng trắng và nó là ký tự đầu tiên hoặc ký tự trước đó là khoảng trắng, thì chúng ta đã tìm thấy một đoạn mới
                count += 1
        return count
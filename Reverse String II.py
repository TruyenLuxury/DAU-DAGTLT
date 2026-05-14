class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s) # Chuyển đổi chuỗi thành một danh sách để có thể thay đổi các ký tự, sau đó duyệt qua chuỗi với bước nhảy là 2k và đảo ngược các ký tự trong khoảng từ i đến i+k, cuối cùng chuyển đổi danh sách trở lại thành chuỗi và trả về kết quả.
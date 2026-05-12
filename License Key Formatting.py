class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-", "").upper()# Loại bỏ tất cả dấu gạch ngang và chuyển đổi tất cả các ký tự thành chữ hoa
        groups = []
        for i in range(len(s), 0, -k):# Bắt đầu từ cuối chuỗi và tạo các nhóm có độ dài k bằng cách lấy các phần con của chuỗi
            start = max(0, i - k)
            groups.append(s[start:i])
        groups.reverse()
        return "-".join(groups)
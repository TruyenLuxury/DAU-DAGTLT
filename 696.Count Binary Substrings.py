class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = []
        count = 1

        # Đếm độ dài từng nhóm ký tự liên tiếp
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # Thêm nhóm cuối

        # Tính tổng min của 2 nhóm liền kề
        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i - 1], groups[i])

        return result
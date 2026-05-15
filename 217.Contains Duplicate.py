class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for x in nums: # Duyệt qua từng phần tử trong mảng
            if x in seen: # Nếu x đã tồn tại trong set, có nghĩa là đã có duplicate
                return True
            seen.add(x)

        return False
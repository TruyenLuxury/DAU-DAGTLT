class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}

        for i, num in enumerate(nums): # Duyệt qua từng phần tử trong mảng cùng với chỉ số của nó
            if num in index_map:
                if i - index_map[num] <= k: # Nếu khoảng cách giữa hai chỉ số nhỏ hơn hoặc bằng k, có nghĩa là đã tìm thấy duplicate gần nhau
                    return True
            
            index_map[num] = i  # cập nhật index mới nhất

        return False
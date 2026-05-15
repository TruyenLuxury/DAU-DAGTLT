class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]# Cập nhật tổng của cửa sổ bằng cách thêm phần tử mới (nums[i]) và trừ phần tử cũ (nums[i - k]) ra khỏi tổng.
            max_sum = max(max_sum, window_sum)
        return max_sum / float(k)
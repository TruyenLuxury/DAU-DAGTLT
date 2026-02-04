class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target: # Nếu tìm thấy target
                return mid
            elif nums[mid] < target:# Nếu target lớn hơn phần tử giữa
                left = mid + 1
            else:# Nếu target nhỏ hơn phần tử giữa
                right = mid - 1
        return left
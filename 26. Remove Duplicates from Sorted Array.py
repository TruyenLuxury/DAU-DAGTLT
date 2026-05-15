class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        if not nums:# Trường hợp mảng rỗng
            return 0 
        for i in range (1,len(nums)):
            if nums [i] != nums [k-1]: # Phần tử sau khác phần tử trước -> giá trị mới
                nums [k] = nums[i]
                k += 1
        return k
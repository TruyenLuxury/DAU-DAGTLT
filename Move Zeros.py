class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):# duyệt qua tất cả phần tử của mảng, nếu phần tử đó khác 0 thì ta sẽ di chuyển nó lên đầu mảng
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos,len(nums)): # sau khi đã di chuyển tất cả các phần tử khác 0 lên đầu mảng, ta sẽ điền 0 vào phần còn lại của mảng
            nums[i] = 0
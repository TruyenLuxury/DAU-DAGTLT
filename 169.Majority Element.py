class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        kt = None
        for num in nums:
            if count == 0:
                kt = num
            if num == kt:
                count += 1
            else:
                count -= 1
        return kt
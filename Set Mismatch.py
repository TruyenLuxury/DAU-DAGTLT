from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        duplicate = missing = 0
        for i in range(1, len(nums) + 1):
            if count[i] == 2:
                duplicate = i    # xuất hiện 2 lần → số trùng
            elif count[i] == 0:
                missing = i      # không xuất hiện → số mất
        return [duplicate, missing]
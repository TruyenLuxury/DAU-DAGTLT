class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        result = []
        for i in range (1,len(nums)+1):
            if i not in s:
                result.append(i)
        return result
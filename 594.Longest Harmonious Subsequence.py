class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        longest = 0
        for num in count:
            if num + 1 in count:
                longest = max(
                    longest,
                    count[num] + count[num + 1]
                )
        return longest
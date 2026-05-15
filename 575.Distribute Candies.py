class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        kinds = len(set(candyType))
        return min(kinds, len(candyType) // 2)
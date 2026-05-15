class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq  = {}  # Tần suất xuất hiện
        first = {}  # Vị trí xuất hiện đầu tiên
        last  = {}  # Vị trí xuất hiện cuối cùng
        for i, n in enumerate(nums):
            freq[n]  = freq.get(n, 0) + 1
            last[n]  = i
            if n not in first:
                first[n] = i
        degree = max(freq.values())  # Tìm degree của array
        result = len(nums)
        for n in freq:
            if freq[n] == degree:
                # Độ dài subarray nhỏ nhất chứa đủ degree lần n
                result = min(result, last[n] - first[n] + 1)
        return result
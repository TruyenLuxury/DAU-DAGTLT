class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_scores = sorted(score, reverse=True)
        rank = {}
        for i, s in enumerate(sorted_scores):# Duyệt qua danh sách điểm đã được sắp xếp và gán thứ hạng tương ứng cho mỗi điểm
            if i == 0:
                rank[s] = "Gold Medal"
            elif i == 1:
                rank[s] = "Silver Medal"
            elif i == 2:
                rank[s] = "Bronze Medal"
            else:
                rank[s] = str(i + 1)
        result = []
        for s in score:
            result.append(rank[s])
        return result
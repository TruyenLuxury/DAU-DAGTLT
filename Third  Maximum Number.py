class Solution:
    def thirdMax(self, nums):
        top3 = sorted(set(nums), reverse=True)
        return top3[2] if len(top3) >= 3 else top3[0] 
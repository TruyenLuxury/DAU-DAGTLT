class Solution:
    def summaryRanges(self, nums):
        res = []
        n = len(nums)

        i = 0
        while i < n:
            start = nums[i]

            # kéo dài range
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1

            # kết thúc range
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(nums[i])) # nếu start khác nums[i], tức là có range, thì thêm "start->nums[i]" vào kết quả
            i += 1

        return res
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        nums = []
        for row in mat:
            for num in row:
                nums.append(num)
        result = []
        index = 0
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(nums[index])
                index += 1
            result.append(new_row)
        return result
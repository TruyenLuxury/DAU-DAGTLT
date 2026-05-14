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
        if m * n != r * c:# Kiểm tra nếu số phần tử trong ma trận ban đầu (m * n) không bằng số phần tử trong ma trận mới (r * c), nếu không thì trả về ma trận ban đầu vì không thể reshape được
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
                new_row.append(nums[index])# Thêm phần tử từ nums vào new_row theo thứ tự, sử dụng index để theo dõi vị trí hiện tại trong nums
                index += 1
            result.append(new_row)
        return result
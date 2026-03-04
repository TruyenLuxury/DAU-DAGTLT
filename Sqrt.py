class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:# Trường hợp đặc biệt khi x là 0 hoặc 1
            return x
        left = 0
        right = x
        ans = 0
        while left <= right:# Sử dụng thuật toán tìm kiếm nhị phân để tìm căn bậc hai của x
            mid = (left + right) // 2
            
            if mid * mid == x:# Nếu mid * mid bằng x, thì mid chính là căn bậc hai của x
                return mid
            elif mid * mid < x:# Nếu mid * mid nhỏ hơn x, thì căn bậc hai của x phải lớn hơn mid
                ans = mid  
                left = mid + 1
            else:# Nếu mid * mid lớn hơn x, thì căn bậc hai của x phải nhỏ hơn mid
                right = mid - 1
        return ans
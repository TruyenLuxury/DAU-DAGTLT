class Solution(object):
    from collections import Counter # Counter là một lớp trong thư viện collections của Python, nó được sử dụng để đếm số lần xuất hiện của các phần tử trong một iterable (như list, tuple, string, v.v.). Counter trả về một đối tượng giống như dictionary, trong đó key là phần tử và value là số lần xuất hiện của phần tử đó trong iterable.
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1) # Đếm số lần xuất hiện của mỗi phần tử trong nums1 và lưu vào count1, count1 là một dictionary có key là phần tử trong nums1 và value là số lần xuất hiện của phần tử đó trong nums1
        count2 = Counter(nums2) # Đếm số lần xuất hiện của mỗi phần tử trong nums2 và lưu vào count2, count2 là một dictionary có key là phần tử trong nums2 và value là số lần xuất hiện của phần tử đó trong nums2
        result = []
        for num in count1:
            if num in count2:
                times = min(count1[num], count2[num])
                result += [num] * times
        return result
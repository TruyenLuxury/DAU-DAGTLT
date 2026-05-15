class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False
        for c in set(ransomNote): 
            if magazine.count(c) < ransomNote.count(c): # Nếu số lần xuất hiện của c trong magazine nhỏ hơn số lần xuất hiện của c trong ransomNote thì ta trả về False, nếu không thì ta tiếp tục kiểm tra các ký tự khác trong ransomNote
                return False
        return True
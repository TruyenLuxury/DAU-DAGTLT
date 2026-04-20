class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp="abcdefghijklmnopqrstuvwxyz"
        for i in temp:
            if s.count(i)!=t.count(i): # nếu số lần xuất hiện của i trong s khác với số lần xuất hiện của i trong t thì
                return False
        return True 
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        chartoword = {}
        wordtochar = {}
        for s,m in zip(pattern,words):
            if s in chartoword and chartoword[s] != m: # nếu s đã được ánh xạ đến một từ nào đó mà khác với m thì trả về False
                return False
            if m in wordtochar and wordtochar[m] != s: # nếu m đã được ánh xạ đến một ký tự nào đó mà khác với s thì trả về False
                return False 
            chartoword[s] = m
            wordtochar[m] = s
        return True
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: # Nếu chuỗi rỗng
            return ""
        gtridau = strs[0] #Lấy phần tử đầu làm giá trị chung
        for s in strs: # Duyệt phần tử trong chuỗi 
            while not s.startswith(gtridau):#Kiểm tra giá trị có bằng giá trị đầu không 
                gtridau = gtridau[:-1] #Rút ngắn giá trị cho đến khi khớp
                if gtridau == "":#Trả về chuỗi rỗng
                    return ""
        return gtridau
class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        if num < 0: # Đối với số âm, chúng ta cần chuyển đổi nó thành dạng bù 2 để có được biểu diễn hexa chính xác. Bù 2 của một số âm được tính bằng cách cộng số đó với 2^32 (đối với số nguyên 32-bit).
            num = num + (1 << 32)
        result = []
        while num:
            result.append(hex_chars[num % 16])# Lấy phần dư khi chia cho 16 để xác định ký tự hexa tương ứng và thêm nó vào kết quả
            num //= 16
        return "".join(reversed(result))# Đảo ngược chuỗi
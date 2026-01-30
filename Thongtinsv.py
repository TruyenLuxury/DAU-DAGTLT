# Hoàng Nhật Truyền
f = open("Hello Python/HocPython/dssv.txt", "a", encoding="utf-8")
print("Đã tạo file thành công")

# Tạo lớp Student
#--------------------
class Student:
    sl = 0
    def __init__(self,hoten,diem):#Khởi tạo hàm
        Student.sl += 1
        self.hoten = hoten
        if Student.sl >= 10:
            self.maSv = "0" + str(Student.sl)
        else:
            self.maSv = "00"+str(Student.sl)
        self.diem = diem
    def __str__(self):
        return f"Họ tên: {self.hoten}\t -Mã SV: {self.maSv}\t-Điểm: {self.diem}"
    
# Tạo lớp quản lý sinh viên
#---------------------

class ManageStudent:
    def __init__(self):
        self.ds = [] #Khởi tạo một danh sách rỗng
    def them_thong_tin(self):
        ten = input("Nhập họ tên sinh viên: ")
        while True:
            try:
                diem = float(input("Nhập điểm của sinh viên [0-10]: "))
                if (diem<0 or diem>10):
                    raise ValueError ("Điểm phải nằm trong khoảng 0 -> 10")
                break
            except Exception as e:
                if "convert" in str(e):
                    print("Điểm phải là một số")
        self.ds.append(Student(ten,diem)) #Thêm sinh viên vừa nhập vào danh sách
    def in_ds(self):
        if (len(self.ds)) == 0: #Kiểm tra độ dài của danh sách
            print("Danh sách rỗng !")
        else:
            for i in self.ds:# Duyệt từng phần tử trong danh sách
                print(i)
    def ghi_sv(self):
        try:
            with open("Hello Python/HocPython/dssv.txt", "w",encoding="utf-8") as f:
                for i in self.ds:
                    f.write(f"{i.maSv},{i.hoten},{i.diem}\n")
                print("Đã ghi file thành công")
        except Exception as s:
            print("Da co loi: ",s)
    def docfile(self):
        self.ds.clear()
        try:
            with open("Hello Python/HocPython/dssv.txt", "r",encoding="utf-8") as g:
                lines = g.readlines()
                for i in lines:
                    m,t,d = i.strip().split(",")
                    Sv = Student(t,d)
                    Sv.maSv = m
                    self.ds.append(Sv)
            print("Đã đọc file thành công")
        except FileNotFoundError:
            print("Không tìm thấy file")
        except Exception as a:
            print("Đã có lỗi: ",a)
# Test chức năng
#--------------
n = ManageStudent()
n.them_thong_tin() #Gọi hàm thêm thông tin
n.them_thong_tin() #Gọi hàm thêm thông tin
n.them_thong_tin()
n.in_ds() #Gọi hàm in danh sách
n.ghi_sv() #Gọi hàm ghi danh sách
n.docfile() #Gọi hàm để đọc file dssv.txt
n.in_ds()# Gọi hàm để iin danh sách
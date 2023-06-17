# Đây là phần in ra đáp án
'''
a = 10
b = "string"
print("a =", a, end = "\n")
print("b =", b)
print("a + b =", a, b)
print("a + b =", str(a) + " " + b, sep = " ")
'''
# comment
#-----------------------
# Họ và tên: Trọng Ánh
#print("Bạn là ai:", input("Họ và tên: "))

# input trả lại kết quả luôn luôn là string

#Ten = input("Tên của bạn: ")
#Ho_dem = input("Họ và tên đệm của bạn: ")

'''
Tuoi = int(input("Tuổi của bạn là bao nhiêu: "))
print(type(Tuoi))
#print("Tên đầy đủ của bạn là:", Ho_dem, Ten)
print("Tuổi hiện tại là:", Tuoi)
'''
'''
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("KQ: (a + b + c)/3 =", (a + b + c)/3)
'''

a = 35205000
b = 1500
c = 1257125

print("1$ =", float(a/b))
print("Số tháng:", a//c + 1)
print("Số tiền của tháng:", c * (a//c + 1) / float(a/b))
#Bài 1
'''
n = int (input("Nhập n = "))
if (n % 2 == 0):
    print("Số chẵn.")
else:
    print("Số lẻ.")
'''    
#Bài 2
'''
dtb = float(input("Điểm trung bình = "))
if (dtb >= 9):
    print("Học sinh giỏi.")
elif (dtb < 9 and dtb >= 7):
    print("Học sinh khá.")
elif (dtb <7 and dtb >= 5):
    print("Học sinh trung bình.")
else:
    print("Học sinh yếu.")
'''

#Bài 3
''' 
nam = int(input("Năm dương lịch = "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Năm nhập vào là năm nhuận.")
else:
    print("Năm nhập vào không phải là năm nhuận.")
'''    

#Bài 4
'''
thang = int(input("Nhập tháng = "))
if (thang in (1,3,5,7,8,10,12)):
    print("Tháng nhập vào có 31 ngày.")
elif (thang in (4,6,9,11)):
    print("Tháng nhập vào có 30 ngày.")
else:
    nam = int(input("Nhập năm = "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng nhập vào có 29.")
    else:
        print("Tháng nhập vào có 28.")
'''

#Bài 5
'''
import math
print("Ta có phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
c = float(input("Nhập c = "))
print(f"Phương trình {a}x^2 + {b}x + {c} = 0")
delta = b**2 - 4*a*c
if (delta < 0):
    print("Vô nghiệm.")
elif (delta == 0):
    print(f"Phương trình có nghiệm kép: x1 = x2 = (-b)/(2a) = {round((-b)/(2*a), 2)}")
else:
    print(f"Phương trình có nghiệm 1: x1 = (-b + căn(delta))/(2a) = {round((-b + math.sqrt(delta))/(2*a), 2)} and x2 = (-b - căn(delta))/(2a) = {round((-b - math.sqrt(delta))/(2*a), 2)}")
'''

#Bài 6
'''
thang = int(input("Nhập tháng = "))
if (thang in (1,2,3)):
    print("Quý 1.")
elif (thang in (4,5,6)):
    print("Quý 2.")
elif (thang in (7,8,9)):
    print("Quý 3.")
else:
    print("Quý 4.")
'''
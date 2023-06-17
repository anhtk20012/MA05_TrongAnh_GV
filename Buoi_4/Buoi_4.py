'''
n = int(input("Nhập n: "))
# Để kiểm tra n là số chẵn thì n phải chia hết cho 2
# Khi nào n chia hết cho 2
# Khi số dư = 0 -> Để lấy số dư thì mình sử dụng phép chia %

print("Chọn 1 là quả táo.")
print("Chọn 2 là quả cam.")
print("Chọn 3 là quả xoài.")
print("Chọn 4 là quả khác.")

qua = int(input("Nhập quả cần bỏ vào giỏ: "))
if (qua == 1):
    print("Bỏ vào giỏ A")
elif (qua == 2):
    print("Bỏ vào giỏ B")
elif (qua == 3):
    print("Bỏ vào giỏ C")
else:
    print("Bỏ vào giỏ D")
'''

n = float(input("Nhập n: "))

if (n > 0):
    print("Trị tuyệt đối của", n, "là:", round(n))
else: 
    print("Trị tuyệt đối của", n , "là:", round(n * (-1)))
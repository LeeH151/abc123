#Bai 1
def kiemtra(a):
    if a < 0:
        return False
    return True
print(kiemtra(5))
#Bai 3
def max():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    if a > b:
        return a
    return b
print("Số lớn nhất là: ",max())
#Bai 4
def tim():
    lst = [1,2,3,4,5,6,7,8,9]
    a = int(input("Nhập: "))
    if a in lst:
        return True
    return False
print(tim())   
#Bai 7
def tuoi(namsinh):
    from datetime import date
    return date.today().year - namsinh
print("Tuổi của bạn là: ",tuoi(2004))
#Bai 8
def nhietdo(f):
    return 5*(f-32)/9
print(nhietdo(100))
#Bai 9
def mua():
    a = int(input("Nhập vào tháng: "))
    if a in[1,2,3]:
        return "Mùa Xuân"
    elif a in[4,5,6]:
        return "Mùa Hạ"
    elif a in[7,8,9]:
        return "Mùa Thu"
    elif a in[10,11,12]:
        return "Mùa Đông"
    return "Không có mùa này"
print(mua())
#Bai 10
def nam(a):
    if a % 4 == 0:
        return "Năm nhuận"
    return "Năm không nhuận"
print(nam(2024))   
#Bai 11
def chu_vi_dien_tich(R):
    PI = 3.14
    CV = 2*PI*R
    DT = PI*R*R
    return [CV,DT]
print(chu_vi_dien_tich(5))
CV,DT = chu_vi_dien_tich(5)
print("Chu vi = ",CV,"\nDiện tích = ",DT)
#Bai 12
def ham():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    sum = a + b
    tbc = sum / 2
    return [sum,tbc]
sum,tbc = ham()
print("Tổng các giá trị: ",sum,"\nTrung bình cộng: ",tbc)
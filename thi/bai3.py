
#gọi hàm
def ho_ten(number):
    str1 = str(number);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return ("là số thuận nghịch")
    else:
        return ("không là số thuận nghịch")
 

#nhập
ten = input("tên: ")
dem=input("tên đệm: ")
ho=input("họ: ")



#đếm
dem1=str(len(ho))
dem2=str(len(dem))
dem3=str(len(ten))
number=dem1+dem2+dem3

#in ra màn hình
print("họ tên đầy đủ; ",ho +" "+dem+" " + ten)
print(number ,"là",ho_ten(number))



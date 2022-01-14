#nhập tên của mình và đếm
name=len(input("nhập tên đệm và tên:  "))


print("độ dài tên của mình là: ", name)


#tính tổng các chữ số
tong = 0
for i in range(len(str(name))):
    chu=name%10
    tong = tong + chu
    name= name//10


#in ra màn hình
print("tổng các chữ số của n là: ", tong)
#nhập vào id sinh viên

name=input("nhập tên  : ")
id=input("nhập id: ")



#in ra màn hình tên và id

print("ten va id: ",name+id)

#phân tách bằng dấu ","
l=(name+id).split(",")


#tạo 1 tuple rỗng
tup=tuple(l)

#in ra màn hình
print ("in ra màn hình tup: ",tup)


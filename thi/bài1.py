"""Bài 1, Hãy viết chương trình để tạo ra một dictionary chứa (i, i*i), trong đó i là số nguyên từ 1 đến n (bao gồm cả 1 và n), 
n được nhập từ bàn phím.
 Sau đó in ra dictionary này ra màn hình. 
 Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}. """



#nhập tên của mình
a= input("nhập tên của mình: ")

#in tên của mình
print("tên của mình là: ",a)

#tính độ dài tên

n =len(str(a))
print("độ dài tên :",n)



#tạo 1 dict rỗng
dictt = dict()

#dictionary chứa (i, i*i)
for i in range(1, n + 1):
    dictt[i] = i * i
    
#in ra màn hình
print("dictionary của độ dài tên là: ",dictt)

a = float(input("Nhap diem :"))
if a >= 8.5 and a <= 10 :
    b = "A" , c = 4
elif a >= 7.0 and a <= 8.4 :
    b = "B" , c = 3
elif a >= 5.5 and a <= 6.9 :
    b = "C" , c = 2
elif a >= 4.0 and a <= 5.4 :
    b = "D" , c = 1
elif a < 4.0 :
    b = "F" , c = 0
print (f"Diem he so 4 la :{b}")
print(f"Theo bang chu cai :{c}")

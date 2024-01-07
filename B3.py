a = []
n = int(input("Nhập do daiarray: "))
array = [int(input(f"Nhập phần tử {i + 1}: ")) for i in range(n)]
for i in array :
    if i not in a :
        a.append(i)
print(a)    

        
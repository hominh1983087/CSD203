def tim_gan_trung_binh(arr):
    tong_array = sum(arr)
    do_dai_array = len(arr)
    trung_binh = tong_array / do_dai_array
    print(trung_binh)

    phan_tu_gan_trung_binh = min(arr, key=lambda x: abs(x - trung_binh))
    print(phan_tu_gan_trung_binh)
    vi_tri = arr.index(phan_tu_gan_trung_binh) + 1  
    print(vi_tri)
    return vi_tri

n = int(input("Nhập số lượng phần tử trong array: "))
array_phantu = [int(input(f"Nhập phần tử {i + 1}: ")) for i in range(n)]

vi_tri = tim_gan_trung_binh(array_phantu)
print(f"Vị trí của phần tử gần giá trị trung bình nhất là: {vi_tri}")
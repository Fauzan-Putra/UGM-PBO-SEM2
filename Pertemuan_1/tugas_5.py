pilihan_user = int(input("Masukkan 1 untuk hitung luas lingkaran, 2 untuk keliling lingkaran: "))
jari_jari = int(input("Masukkan nilai jari-jari lingkaran: "))

def rumus_luas_lingkaran():
    print(3.14 * jari_jari**2)

def rumus_keliling_lingkaran():
    print(3.14*2*jari_jari)


if pilihan_user == 1:
    rumus_luas_lingkaran()
elif pilihan_user == 2:
    rumus_keliling_lingkaran()
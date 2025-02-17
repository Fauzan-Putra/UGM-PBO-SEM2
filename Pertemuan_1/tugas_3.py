NIU = int(input("Masukkan 6 digit NIU: "))
nilai_tugas = int(input("Masukkan nilai tugas: "))
nilai_laporan = int(input("Masukkan nilai laporan: "))
rata_rata = (nilai_laporan + nilai_tugas)/2

if rata_rata < 40:
    print("Nilai siswa: K")
    exit()
else:
    nilai_ujian = int(input("Masukkan nilai ujian: "))
    nilai_akhir = (nilai_tugas*0.25) + (nilai_laporan*0.25) + (nilai_ujian*0.5)
    if nilai_akhir >= 80 and nilai_akhir <= 100:
        print("Nilai siswa: A")
    elif nilai_akhir >= 70 and nilai_akhir < 80:
        print("Nilai siswa: B")
    elif nilai_akhir >= 60 and nilai_akhir < 70:
        print("Nilai siswa: C")
    elif nilai_akhir >= 50 and nilai_akhir < 60:
        print("Nilai siswa: D")
    elif nilai_akhir < 50:
        print("Nilai siswa: E")
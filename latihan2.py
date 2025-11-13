data = []

while True:
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas (30%): "))
    uts = float(input("Masukkan nilai UTS (35%): "))
    uas = float(input("Masukkan nilai UAS (35%): "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data.append([nama, tugas, uts, uas, nilai_akhir])

    lanjut = input("Tambah data lagi? (y/t): ")
    if lanjut.lower() == "t":
        break

print("\nDaftar Nilai Mahasiswa")
print("="*50)
print("Nama\t\tTugas\tUTS\tUAS\tNilai Akhir")
print("-"*50)
for d in data:
    print(f"{d[0]}\t\t{d[1]}\t{d[2]}\t{d[3]}\t{d[4]:.2f}")
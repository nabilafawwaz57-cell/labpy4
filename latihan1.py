A = [10, 20, 30, 40, 50]

print("Elemen ke-3:", A[2])
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terakhir:", A[-1])

A[3] = 99
print("List setelah ubah elemen ke-4:", A)

A[3:] = [99, 100, 101]
print("List setelah ubah elemen ke-4 sampai terakhir:", A)

B = A[:2]
print("List B (2 bagian dari A):", B)

B.append("Python")
print("List B setelah tambah string:", B)

B.extend([60, 70, 80])
print("List B setelah tambah 3 nilai:", B)

C = B + A
print("Gabungan list B dan A:", C)
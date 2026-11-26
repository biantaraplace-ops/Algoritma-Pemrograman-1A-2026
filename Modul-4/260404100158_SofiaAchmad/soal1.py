baris = int(input("Jumlah baris lampu: "))
lampu = int(input("Jumlah lampu tiap baris: "))

for i in range(1, baris + 1):
    print("Baris", i)
    for j in range(1, lampu + 1):
        if j % 3 == 0:
            print("  Lampu", j, "gangguan")
        else:
            print("  Lampu", j, "normal")

print("Periksa sumber listrik utama taman!")
def cek_kelayakan(pc):
    status = pc[1]
    ram = int(pc[2])  
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"
 
 
jumlah = int(input("\nMasukkan jumlah PC: "))
inventaris = []
 
for i in range(jumlah):
    print("Data PC ke-", i + 1)
    nama_pc = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama_pc, status, ram])
 
print("\n=== Hasil Evaluasi ===")
for pc in inventaris:
    try:
        hasil = cek_kelayakan(pc)
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')
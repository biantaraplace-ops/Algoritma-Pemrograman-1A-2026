list_asisten = []
asisten = input("\nMasukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")
while asisten != "cukup":
    list_asisten.append(asisten)
    asisten = input("Masukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")
asisten_awal = tuple(list_asisten)
 
tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)
 
list_hari = []
hari = input("Masukkan nama hari tugas (ketik 'cukup' untuk berhenti): ")
while hari != "cukup":
    list_hari.append(hari)
    hari = input("Masukkan nama hari tugas (ketik 'cukup' untuk berhenti): ")
hari_tugas = tuple(list_hari)
 
asisten_kecuali = input("Masukkan nama asisten pengecualian: ")
hari_kecuali = input("Masukkan hari pengecualian: ")
 
print("\n=== Jadwal Shift ===")
for a in asisten_akhir:
    for h in hari_tugas:
        if a == asisten_kecuali and h == hari_kecuali:
            continue
        print(a, "-", h)
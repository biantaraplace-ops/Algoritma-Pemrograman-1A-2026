daftar_nama = []
 
nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
while nama != "selesai":
    daftar_nama.append(nama)
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
 
print("\n=== Hasil Pemeriksaan ===")
for n in daftar_nama:
    if n == "admin" or len(n) < 4:
        print(n, "-> nama tidak valid")
    else:
        print(n, "-> nama valid")
 
penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")
if penyusup in daftar_nama:
    daftar_nama.remove(penyusup)
    print(penyusup, "berhasil dihapus")
else:
    print(penyusup, "tidak ada di pendaftaran")
 
print("Daftar nama sekarang:", daftar_nama)

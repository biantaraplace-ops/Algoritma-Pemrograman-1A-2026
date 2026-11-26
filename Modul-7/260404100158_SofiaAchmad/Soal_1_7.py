tugas = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1": 
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum Selesai"
        print("Tugas berhasil ditambahkan!")

    elif pilih == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            for nama, status in tugas.items():
                print(nama, ":", status)

    elif pilih == "3":
        nama = input("Tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil diselesaikan!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "4":
        nama = input("Tugas yang dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "5":
        selesai = list(tugas.values()).count("Selesai")
        belum = list(tugas.values()).count("Belum Selesai")
        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilih == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")

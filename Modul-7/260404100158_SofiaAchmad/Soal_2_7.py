playlist = {}

while True:
    print("\n=== MENU PLAYLIST MUSIK ===")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        playlist[nama] = {}
        print("Playlist berhasil dibuat!")

    elif pilih == "2":
        nama = input("Nama playlist: ")

        if nama in playlist:
            lagu = input("Judul lagu: ")
            penyanyi = input("Nama penyanyi: ")
            playlist[nama][lagu] = penyanyi
            print("Lagu berhasil ditambahkan!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)
                for judul, penyanyi in lagu.items():
                    print(judul, "-", penyanyi)

    elif pilih == "4":
        cari = input("Judul lagu: ")
        ketemu = False

        for nama, lagu in playlist.items():
            if cari in lagu:
                print("Lagu ditemukan!")
                print("Playlist:", nama)
                print("Penyanyi:", lagu[cari])
                ketemu = True

        if not ketemu:
            print("Lagu tidak ditemukan.")

    elif pilih == "5":
        nama = input("Nama playlist: ")

        if nama in playlist:
            lagu = input("Judul lagu yang dihapus: ")

            if lagu in playlist[nama]:
                del playlist[nama][lagu]
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "6":
        nama = input("Nama playlist yang dihapus: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
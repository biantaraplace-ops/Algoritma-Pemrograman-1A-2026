def pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pelanggan(n - 1) + pelanggan(n - 2)

N = int(input("Masukkan hari ke-N : "))

print("Pelanggan sampai hari ke-", N, ":")
for hari in range(1, N + 1):
    print("Hari ke-", hari, ":", pelanggan(hari), "orang")

print("Jumlah pelanggan hari ke-", N, "=", pelanggan(N), "orang")
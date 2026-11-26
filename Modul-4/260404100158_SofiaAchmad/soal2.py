total = 0

for hari in range(1, 8):
    print("Hari ke-", hari)
    gaji = 100000

    lembur = int(input("Jam lembur: "))
    while lembur < 0 or lembur == 5 or lembur == 7:
        print("Jam lembur tidak sesuai, input lagi!")
        lembur = int(input("Jam lembur: "))

    if lembur >= 1 and lembur <= 3:
        gaji += lembur * 25000
    elif lembur == 4:
        gaji += 100000
    elif lembur == 6:
        gaji += 200000
    elif lembur == 8:
        gaji += 300000
    elif lembur > 8:
        print("Lembur melebihi batas, tidak dihitung")

    shift = input("Shift malam? (y/t): ")
    if shift == "y":
        gaji += 50000

    print("Gaji hari ini: Rp", gaji)
    total += gaji

print("Total gaji seminggu: Rp", total)
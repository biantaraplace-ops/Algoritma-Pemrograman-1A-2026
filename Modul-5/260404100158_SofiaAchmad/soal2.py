def palindrom(kata):
    terbalik = ""
    for huruf in kata:
        terbalik = huruf + terbalik
    if kata == terbalik:
        return True
    else:
        return False

kata = str(input("Masukkan kata : "))
hasil = palindrom(kata)
print("Hasil fungsi :", hasil)
if hasil == True:
    print("Kata", kata, "adalah palindrom")
else:
    print("Kata", kata, "bukan palindrom")
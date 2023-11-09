angka = int(input("masukkan angka berapapun: "))

a = 5
c = 10
m = 2**7

jumlah_angka_acak = int(input("masukkan banyak angka yang ingin dikeluarkan: "))

angka_acak = angka

for angka in range(jumlah_angka_acak):
    angka_acak = (a * angka_acak + c) % m
    angka_akhir = 1 + (angka_acak % 100)
    print(angka_akhir)
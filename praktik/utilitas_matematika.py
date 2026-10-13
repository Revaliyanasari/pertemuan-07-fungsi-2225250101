def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")


def main():
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas persegi panjang:", luas_persegi_panjang(p, l))
    elif pilihan == "2":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print("Luas segitiga:", luas_segitiga(alas, tinggi))
    elif pilihan == "3":
        n = int(input("Masukkan n: "))
        print("Jumlah 1 sampai", n, ":", jumlah_n(n))
    elif pilihan == "4":
        n = int(input("Masukkan n: "))
        print("Faktorial", n, ":", faktorial(n))
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
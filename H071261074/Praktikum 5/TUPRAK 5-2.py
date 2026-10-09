
def cek_kata(teks, kata):
    indeks = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    awal = 0

    if kata == "":
        return indeks

    while True:
        posisi = teks_kecil.find(kata_kecil, awal)

        if posisi == -1:
            break

        indeks.append(posisi)
        awal = posisi + 1
    print("Indeks kata target:", indeks)

    return indeks


def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    if i > 0:
        if teks[i - 1].lower() in alfabet:
            return False

    akhir = i + panjang

    if akhir < len(teks):
        if teks[akhir].lower() in alfabet:
            return False

    return True


def sensor_kata(teks, kata, simbol):
    posisi_kata = cek_kata(teks, kata)
    hasil = ""
    indeks_valid = []
    awal = 0
    jumlah = 0

    for i in posisi_kata:
        if cek_batas_kata(teks, i, len(kata)):
            if i >= awal:
                hasil += teks[awal:i]
                hasil += simbol * len(kata)

                awal = i + len(kata)
                indeks_valid.append(i)
                jumlah += 1

    hasil += teks[awal:]

    return hasil, jumlah, indeks_valid


teks = input("Masukkan teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Hasil teks:", hasil)
print(f"Jumlah: {jumlah} | Indeks: {indeks}")
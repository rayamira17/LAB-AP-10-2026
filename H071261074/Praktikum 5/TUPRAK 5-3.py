ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
  is_upper = ch.isupper()
  ch_lower = ch.lower()

  if ch_lower in ALFABET:
    idx = ALFABET.find(ch_lower)
    new_idx = (idx + k) % 26
    hasil_ch = ALFABET[new_idx]
    return hasil_ch.upper() if is_upper else hasil_ch
  else:
    return ch


def mesin_enkripsi(teks, k):
  hasil = ""
  for char in teks:
    hasil += cek_sandi(char, k)
  return hasil


def mesin_dekripsi(teks, k):
  return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
  hasil_retas = []
  for k in range(26):
    pesan_dekrip = mesin_dekripsi(sandi, k)
    
    if pesan_dekrip.lower().find(kata_kunci.lower()) != -1:
      hasil_retas.append((k, pesan_dekrip))
  return hasil_retas

if __name__ == "__main__":
  pesan_tersita = input("Masukkan pesan tersita (enkripsi Caesar): ")
  kata_kunci_target = input("Masukkan kata kunci target: ")

  hasil_output = retas_sandi(pesan_tersita, kata_kunci_target)
  print(f"Output Deskripsi: {hasil_output}")

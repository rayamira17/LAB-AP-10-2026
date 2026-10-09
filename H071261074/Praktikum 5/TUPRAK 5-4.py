def deteksi_anomali_email(email, daftar_terdaftar):
  pelanggaran = []

  if email.count("@") != 1:
    pelanggaran.append("Harus memiliki tepat satu karakter @.")
    return pelanggaran

  parts = email.split("@")
  local = parts[0]
  domain = parts[1]

  if local == "" or domain == "":
    pelanggaran.append(
        "Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong."
    )

  if " " in email:
    pelanggaran.append("Tidak boleh mengandung spasi di posisi manapun.")

  if local.startswith(".") or local.endswith("."):
    pelanggaran.append(
        "Bagian local tidak boleh diawali atau diakhiri titik (.)."
    )
  if ".." in local:
    pelanggaran.append(
        "Bagian local tidak boleh mengandung titik berurutan (..)."
    )

  if "." not in domain:
    pelanggaran.append("Bagian domain wajib memiliki minimal satu titik.")
  if ".." in domain:
    pelanggaran.append(
        "Bagian domain tidak boleh mengandung titik berurutan (..)."
    )
  if domain.endswith("."):
    pelanggaran.append(
        "Bagian domain tidak boleh diakhiri titik."
    )

  domain_resmi = (".com", ".id", ".ac.id")
  if not domain.endswith(domain_resmi):
    pelanggaran.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

  if email in daftar_terdaftar:
    pelanggaran.append("Email sudah terdaftar (Duplikat).")

  return pelanggaran


def cetak_daftar(daftar_email_valid, karakter_border):
  if not daftar_email_valid:
    print("Tidak ada email valid untuk dicetak.")
    return

  max_len = max(len(email) for email in daftar_email_valid)

  padding = 2
  lebar_baris = max_len + (padding * 2)

  garis_pembatas = karakter_border * (lebar_baris + 2)

  print(garis_pembatas)
  print(f"| {'HASIL EMAIL VALID'.center(lebar_baris)} |")
  print(garis_pembatas)

  for email in daftar_email_valid:
    email_format = email.ljust(max_len)
    print(f"| {' ' * padding}{email_format}{' ' * padding} |")

  print(garis_pembatas)

if __name__ == "__main__":
  print("--- Sistem Pencatatan email valid ---")
  karakter_border = input("Masukkan border dengan karakter bebas: ")
  print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

  email_terdaftar = []
  email_valid_list = []

  while True:
    masukan_email = input("Masukkan email: ")

    if masukan_email.lower() == "tutup":
      break

    error_list = deteksi_anomali_email(masukan_email, email_valid_list)

    if len(error_list) == 0:
      print(">> Email VALID!")
      email_valid_list.append(masukan_email)
    else:
      print(">> Email DITOLAK karena:")
      for err in error_list:
        print(err)

  print()
  cetak_daftar(email_valid_list, karakter_border)
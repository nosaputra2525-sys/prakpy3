def input_angka(prompt, tipe, minimum, maksimum):
    while True:
        try:
            nilai = tipe(input(prompt))
        except ValueError:
            print("  Input harus berupa angka.")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Nilai harus antara {minimum} dan {maksimum}.")


def input_nim(prompt):
    while True:
        nim = input(prompt).strip()
        if nim.isdigit() and len(nim) == 10:
            return nim
        print("  NIM harus 10 digit angka.")


def tentukan_status(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif"
    if ipk < 2.0:
        return "Peringatan"
    if sks >= 18:
        return "Aktif"
    return "Peringatan"  # IPK >= 2.0 tapi SKS < 18


def main():
    jumlah = 5
    data = []
    print("=== INPUT DATA 5 MAHASISWA ===")
    for i in range(1, jumlah + 1):
        print(f"\nMahasiswa ke-{i}")
        nim = input_nim("  NIM  : ")
        nama = input("  Nama : ").strip()
        ipk = input_angka("  IPK  : ", float, 0.0, 4.0)
        sks = input_angka("  SKS  : ", int, 0, 24)
        data.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks,
                     "status": tentukan_status(ipk, sks)})

    print("\n" + "=" * 70)
    print("LAPORAN STATUS MAHASISWA".center(70))
    print("=" * 70)
    print(f"{'No':<4}{'NIM':<13}{'Nama':<20}{'IPK':<7}{'SKS':<6}{'Status'}")
    print("-" * 70)
    for no, m in enumerate(data, 1):
        print(f"{no:<4}{m['nim']:<13}{m['nama']:<20}{m['ipk']:<7.2f}{m['sks']:<6}{m['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()  
def validasi_mahasiswa(nim, ipk, sks, semester):
    """Mengembalikan list error. List kosong berarti semua data valid."""
    errors = []

    # NIM: 10 digit angka, 4 digit pertama = tahun 2000-2037
    if not (nim.isdigit() and len(nim) == 10):
        errors.append("NIM harus 10 digit angka.")
    else:
        tahun = int(nim[:4])
        if not 2000 <= tahun <= 2037:
            errors.append(f"Tahun pada NIM ({tahun}) harus antara 2000-2037.")

    # IPK
    try:
        nilai_ipk = float(ipk)
        if not 0.0 <= nilai_ipk <= 4.0:
            errors.append("IPK harus antara 0.0 dan 4.0.")
    except ValueError:
        errors.append("IPK harus berupa angka.")

    # SKS
    try:
        nilai_sks = int(sks)
        if not 0 <= nilai_sks <= 24:
            errors.append("SKS harus antara 0 dan 24.")
    except ValueError:
        errors.append("SKS harus berupa bilangan bulat.")

    # Semester
    try:
        nilai_smt = int(semester)
        if not 1 <= nilai_smt <= 14:
            errors.append("Semester harus antara 1 dan 14.")
    except ValueError:
        errors.append("Semester harus berupa bilangan bulat.")

    return errors


def main():
    print("=== VALIDASI DATA MAHASISWA ===")
    nim = input("NIM      : ").strip()
    ipk = input("IPK      : ").strip()
    sks = input("SKS      : ").strip()
    semester = input("Semester : ").strip()

    errors = validasi_mahasiswa(nim, ipk, sks, semester)

    print("\n--- HASIL VALIDASI ---")
    if errors:
        print(f"Ditemukan {len(errors)} kesalahan:")
        for no, e in enumerate(errors, 1):
            print(f"  {no}. {e}")
    else:
        print("Semua data valid.")


if __name__ == "__main__":
    main()
def input_spp(prompt):
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("  Input harus berupa angka.")
            continue
        if nilai > 0:
            return nilai
        print("  SPP harus lebih dari 0.")


def input_angka(prompt, minimum, maksimum):
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("  Input harus berupa angka.")
            continue
        if minimum <= nilai <= maksimum:
            return nilai
        print(f"  Nilai harus antara {minimum} dan {maksimum}.")


def input_yn(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Isi dengan 'y' atau 'n'.")


def hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu):
    rincian = []
    if anak_karyawan:
        rincian.append(("Anak karyawan", 25))
    if ipk >= 3.8:
        rincian.append(("IPK >= 3.8", 20))
    elif ipk >= 3.5:
        rincian.append(("IPK >= 3.5", 15))
    elif ipk >= 3.0:
        rincian.append(("IPK >= 3.0", 10))
    if tepat_waktu:
        rincian.append(("Bayar tepat waktu", 5))

    total_persen = sum(p for _, p in rincian)
    potongan = spp * total_persen / 100
    return rincian, total_persen, potongan, spp - potongan


def main():
    print("=== KALKULATOR DISKON BIAYA KULIAH ===")
    spp = input_spp("Biaya SPP (Rp)             : ")
    anak_karyawan = input_yn("Anak karyawan? (y/n)        : ")
    ipk = input_angka("IPK                        : ", 0.0, 4.0)
    tepat_waktu = input_yn("Bayar tepat waktu? (y/n)    : ")

    rincian, total_persen, potongan, final = hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu)

    print("\n" + "-" * 40)
    print("RINCIAN DISKON")
    if rincian:
        for nama, persen in rincian:
            print(f"  - {nama:<22}: {persen}%")
    else:
        print("  Tidak ada diskon yang berlaku.")
    print("-" * 40)
    print(f"Total diskon  : {total_persen}%")
    print(f"Biaya awal    : Rp {spp:,.0f}")
    print(f"Potongan      : Rp {potongan:,.0f}")
    print(f"Biaya final   : Rp {final:,.0f}")
    print("-" * 40)


if __name__ == "__main__":
    main()
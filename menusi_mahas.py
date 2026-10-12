# ===================== DATA & HELPER =====================
inventaris = [
    {"nama": "Kertas A4",     "stok": 120, "minimum": 50,  "harga": 55000},
    {"nama": "Spidol",        "stok": 30,  "minimum": 40,  "harga": 8000},
    {"nama": "Tinta Printer", "stok": 8,   "minimum": 20,  "harga": 95000},
    {"nama": "Map Folder",    "stok": 0,   "minimum": 25,  "harga": 3000},
    {"nama": "Pulpen",        "stok": 200, "minimum": 100, "harga": 3500},
    {"nama": "Buku Tulis",    "stok": 45,  "minimum": 50,  "harga": 6000},
    {"nama": "Stapler",       "stok": 2,   "minimum": 10,  "harga": 25000},
    {"nama": "Lakban",        "stok": 0,   "minimum": 15,  "harga": 12000},
    {"nama": "Penghapus",     "stok": 90,  "minimum": 30,  "harga": 2000},
]
PRIORITAS = {"Habis": 1, "Rendah": 2, "Peringatan": 3, "Aman": 4}


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


def input_yn(prompt):
    while True:
        jawab = input(prompt).strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("  Isi dengan 'y' atau 'n'.")


# ===================== 1. STATUS MAHASISWA =====================
def tentukan_status(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif"
    if ipk < 2.0:
        return "Peringatan"
    if sks >= 18:
        return "Aktif"
    return "Peringatan"


def menu_status_mahasiswa():
    print("\n=== CEK STATUS MAHASISWA (5 data) ===")
    data = []
    for i in range(1, 6):
        print(f"\nMahasiswa ke-{i}")
        nim = input_nim("  NIM  : ")
        nama = input("  Nama : ").strip()
        ipk = input_angka("  IPK  : ", float, 0.0, 4.0)
        sks = input_angka("  SKS  : ", int, 0, 24)
        data.append((nim, nama, ipk, sks, tentukan_status(ipk, sks)))

    print("\n" + "=" * 70)
    print(f"{'No':<4}{'NIM':<13}{'Nama':<20}{'IPK':<7}{'SKS':<6}{'Status'}")
    print("-" * 70)
    for no, (nim, nama, ipk, sks, status) in enumerate(data, 1):
        print(f"{no:<4}{nim:<13}{nama:<20}{ipk:<7.2f}{sks:<6}{status}")
    print("=" * 70)


# ===================== 2. DISKON BIAYA =====================
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
    total = sum(p for _, p in rincian)
    potongan = spp * total / 100
    return rincian, total, potongan, spp - potongan


def menu_diskon():
    print("\n=== HITUNG DISKON BIAYA KULIAH ===")
    spp = input_angka("Biaya SPP (Rp)          : ", float, 1, 1_000_000_000)
    anak = input_yn("Anak karyawan? (y/n)     : ")
    ipk = input_angka("IPK                     : ", float, 0.0, 4.0)
    waktu = input_yn("Bayar tepat waktu? (y/n) : ")

    rincian, total, potongan, final = hitung_diskon(spp, anak, ipk, waktu)
    print("\n" + "-" * 40)
    if rincian:
        for nama, persen in rincian:
            print(f"  - {nama:<22}: {persen}%")
    else:
        print("  Tidak ada diskon yang berlaku.")
    print("-" * 40)
    print(f"Total diskon : {total}%")
    print(f"Biaya awal   : Rp {spp:,.0f}")
    print(f"Potongan     : Rp {potongan:,.0f}")
    print(f"Biaya final  : Rp {final:,.0f}")
    print("-" * 40)


# ===================== 3. PERINGATAN STOK =====================
def evaluasi_status(stok, minimum):
    if stok == 0:
        return "Habis"
    if stok <= minimum * 0.5:
        return "Rendah"
    if stok <= minimum:
        return "Peringatan"
    return "Aman"


def menu_stok():
    print("\n=== PERINGATAN STOK ===")
    for it in inventaris:
        it["status"] = evaluasi_status(it["stok"], it["minimum"])
        it["prioritas"] = PRIORITAS[it["status"]]
        it["nilai"] = it["stok"] * it["harga"]

    urut = sorted(inventaris, key=lambda x: x["prioritas"])
    print("=" * 84)
    print(f"{'Prio':<6}{'Item':<16}{'Stok':<8}{'Min':<8}{'Harga':>10}{'Nilai':>14}   {'Status'}")
    print("-" * 84)
    for it in urut:
        print(f"{it['prioritas']:<6}{it['nama']:<16}{it['stok']:<8}{it['minimum']:<8}"
              f"{it['harga']:>10,}{it['nilai']:>14,}   {it['status']}")
    print("=" * 84)

    total_nilai = sum(it["nilai"] for it in inventaris)
    restock = sum(1 for it in inventaris if it["status"] != "Aman")
    print(f"Total nilai inventaris : Rp {total_nilai:,}")
    print(f"Rata-rata stok         : {sum(i['stok'] for i in inventaris) / len(inventaris):.1f}")
    for status in PRIORITAS:
        print(f"Item {status:<11}       : {sum(1 for i in inventaris if i['status'] == status)}")
    print(f"Perlu restock          : {restock} item ({restock / len(inventaris) * 100:.1f}%)")


# ===================== MENU UTAMA =====================
def main():
    while True:
        print("\n" + "=" * 40)
        print("   MENU SI MAHASISWA".center(40))
        print("=" * 40)
        print("1. Cek Status Mahasiswa")
        print("2. Hitung Diskon Biaya")
        print("3. Cek Peringatan Stok")
        print("0. Keluar")
        pilihan = input("Pilih menu (0-3): ").strip()

        if pilihan == "1":
            menu_status_mahasiswa()
        elif pilihan == "2":
            menu_diskon()
        elif pilihan == "3":
            menu_stok()
        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, masukkan angka 0-3.")


if __name__ == "__main__":
    main()
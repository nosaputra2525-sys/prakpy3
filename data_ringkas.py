# Data contoh (bisa kamu ganti sesuai kebutuhan)
mahasiswa = [
    {"nim": "2023010001", "ipk": 3.85, "sks": 20},
    {"nim": "2023010002", "ipk": 2.50, "sks": 18},
    {"nim": "2023010003", "ipk": 1.70, "sks": 15},
    {"nim": "2023010004", "ipk": 1.20, "sks": 12},
    {"nim": "2023010005", "ipk": 3.10, "sks": 22},
]

kasus_diskon = [  # (spp, anak_karyawan, ipk, tepat_waktu)
    (5_000_000, True,  3.85, True),
    (5_000_000, False, 3.60, True),
    (5_000_000, False, 3.20, False),
    (5_000_000, True,  2.80, False),
    (5_000_000, False, 2.50, True),
]

inventaris = [
    {"nama": "Kertas A4",     "stok": 120, "minimum": 50},
    {"nama": "Spidol",        "stok": 30,  "minimum": 40},
    {"nama": "Tinta Printer", "stok": 8,   "minimum": 20},
    {"nama": "Map Folder",    "stok": 0,   "minimum": 25},
    {"nama": "Pulpen",        "stok": 200, "minimum": 100},
    {"nama": "Buku Tulis",    "stok": 45,  "minimum": 50},
    {"nama": "Stapler",       "stok": 2,   "minimum": 10},
    {"nama": "Lakban",        "stok": 0,   "minimum": 15},
    {"nama": "Penghapus",     "stok": 90,  "minimum": 30},
]


def status_mahasiswa(ipk, sks):
    if ipk < 1.5:
        return "Tidak Aktif"
    if ipk < 2.0:
        return "Peringatan"
    return "Aktif" if sks >= 18 else "Peringatan"


def persen_diskon(anak_karyawan, ipk, tepat_waktu):
    total = 25 if anak_karyawan else 0
    if ipk >= 3.8:
        total += 20
    elif ipk >= 3.5:
        total += 15
    elif ipk >= 3.0:
        total += 10
    if tepat_waktu:
        total += 5
    return total


def status_stok(stok, minimum):
    if stok == 0:
        return "Habis"
    if stok <= minimum * 0.5:
        return "Rendah"
    if stok <= minimum:
        return "Peringatan"
    return "Aman"


def main():
    # (a) Persentase mahasiswa aktif vs tidak aktif
    total_mhs = len(mahasiswa)
    status_list = [status_mahasiswa(m["ipk"], m["sks"]) for m in mahasiswa]
    aktif = status_list.count("Aktif")
    peringatan = status_list.count("Peringatan")
    tidak_aktif = status_list.count("Tidak Aktif")

    # (b) Rata-rata diskon
    diskon_list = [persen_diskon(k, i, t) for _, k, i, t in kasus_diskon]
    rata_diskon = sum(diskon_list) / len(diskon_list)

    # (c) Persentase item perlu restock (status selain Aman)
    total_item = len(inventaris)
    restock = sum(1 for it in inventaris if status_stok(it["stok"], it["minimum"]) != "Aman")

    print("=" * 62)
    print("RINGKASAN ALGORITMA".center(62))
    print("=" * 62)
    print(f"{'Studi Kasus':<28}{'Metrik':<20}{'Hasil':>12}")
    print("-" * 62)
    print(f"{'(a) Status Mahasiswa':<28}{'Aktif':<20}{aktif / total_mhs * 100:>11.1f}%")
    print(f"{'':<28}{'Peringatan':<20}{peringatan / total_mhs * 100:>11.1f}%")
    print(f"{'':<28}{'Tidak Aktif':<20}{tidak_aktif / total_mhs * 100:>11.1f}%")
    print("-" * 62)
    print(f"{'(b) Diskon Biaya':<28}{'Rata-rata diskon':<20}{rata_diskon:>11.1f}%")
    print("-" * 62)
    print(f"{'(c) Stok Inventaris':<28}{'Perlu restock':<20}{restock / total_item * 100:>11.1f}%")
    print("=" * 62)


if __name__ == "__main__":
    main()   
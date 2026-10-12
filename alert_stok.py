inventaris = [
    {"nama": "Kertas A4",      "stok": 120, "minimum": 50,  "harga": 55000},
    {"nama": "Spidol",         "stok": 30,  "minimum": 40,  "harga": 8000},
    {"nama": "Tinta Printer",  "stok": 8,   "minimum": 20,  "harga": 95000},
    {"nama": "Map Folder",     "stok": 0,   "minimum": 25,  "harga": 3000},
    {"nama": "Pulpen",         "stok": 200, "minimum": 100, "harga": 3500},
    {"nama": "Buku Tulis",     "stok": 45,  "minimum": 50,  "harga": 6000},
    {"nama": "Stapler",        "stok": 2,   "minimum": 10,  "harga": 25000},
    {"nama": "Lakban",         "stok": 0,   "minimum": 15,  "harga": 12000},
    {"nama": "Penghapus",      "stok": 90,  "minimum": 30,  "harga": 2000},
]

PRIORITAS = {"Habis": 1, "Rendah": 2, "Peringatan": 3, "Aman": 4}


def evaluasi_status(stok, minimum):
    if stok == 0:
        return "Habis"
    if stok <= minimum * 0.5:
        return "Rendah"
    if stok <= minimum:
        return "Peringatan"
    return "Aman"


def main():
    for item in inventaris:
        item["status"] = evaluasi_status(item["stok"], item["minimum"])
        item["prioritas"] = PRIORITAS[item["status"]]
        item["nilai"] = item["stok"] * item["harga"]

    urut = sorted(inventaris, key=lambda x: x["prioritas"])

    print("=" * 84)
    print("LAPORAN PERINGATAN STOK".center(84))
    print("=" * 84)
    print(f"{'Prio':<6}{'Item':<16}{'Stok':<8}{'Min':<8}{'Harga':>10}{'Nilai':>14}   {'Status'}")
    print("-" * 84)
    for it in urut:
        print(f"{it['prioritas']:<6}{it['nama']:<16}{it['stok']:<8}{it['minimum']:<8}"
              f"{it['harga']:>10,}{it['nilai']:>14,}   {it['status']}")
    print("=" * 84)

    total_nilai = sum(it["nilai"] for it in inventaris)
    jumlah = len(inventaris)
    rata_stok = sum(it["stok"] for it in inventaris) / jumlah
    termahal = max(inventaris, key=lambda x: x["nilai"])
    perlu_restock = [it for it in inventaris if it["status"] != "Aman"]

    print("\nRINGKASAN STATISTIK")
    print("-" * 40)
    print(f"Total item            : {jumlah}")
    print(f"Total nilai inventaris: Rp {total_nilai:,}")
    print(f"Rata-rata stok        : {rata_stok:.1f}")
    print(f"Nilai item terbesar   : {termahal['nama']} (Rp {termahal['nilai']:,})")
    for status in PRIORITAS:
        n = sum(1 for it in inventaris if it["status"] == status)
        print(f"Item {status:<11}      : {n}")
    print(f"Perlu restock         : {len(perlu_restock)} item "
          f"({len(perlu_restock) / jumlah * 100:.1f}%)")
    print("-" * 40)


if __name__ == "__main__":
    main()
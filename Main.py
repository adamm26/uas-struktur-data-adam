# Data Produk Vape dalam List of Dictionaries
produk_vape = [
    {"kode": 301, "nama": "Vape A", "rasa": "Mint", "harga": 600000, "stok": 0},
    {"kode": 302, "nama": "Vape B", "rasa": "Grape", "harga": 300000, "stok": 0},
    {"kode": 303, "nama": "Vape C", "rasa": "Strawberry", "harga": 250000, "stok": 0},
]

# Data Pelanggan
pelanggan = []

# Stack untuk menyimpan transaksi (Fitur Stack)
stack_transaksi = []

# Fungsi untuk menampilkan daftar produk vape
def tampilkan_produk():
    print("\nDaftar Produk Vape:")
    for produk in produk_vape:
        print(f"Kode: {produk['kode']} | Nama: {produk['nama']} | Rasa: {produk['rasa']} | Harga: Rp {produk['harga']} | Stok: {produk['stok']}")

# Fungsi untuk menambah stok produksi produk vape
def produksi_vape(kode_produk, jumlah):
    for produk in produk_vape:
        if produk["kode"] == kode_produk:
            produk["stok"] += jumlah
            print(f"Produksi {produk['nama']} sebanyak {jumlah} unit berhasil ditambahkan. Stok saat ini: {produk['stok']}")
            return
    print("Kode produk tidak ditemukan.")

# Fungsi untuk memproses penjualan produk vape
def penjualan_vape(kode_produk, jumlah, nama_pelanggan):
    for produk in produk_vape:
        if produk["kode"] == kode_produk:
            if produk["stok"] >= jumlah:
                total_harga = produk["harga"] * jumlah
                produk["stok"] -= jumlah
                print(f"Penjualan {produk['nama']} sebanyak {jumlah} berhasil. Total harga: Rp {total_harga}")
                
                # Tambahkan transaksi ke dalam stack
                stack_transaksi.append({
                    "kode_produk": kode_produk,
                    "jumlah": jumlah,
                    "produk": produk["nama"]
                })
            else:
                print(f"Stok {produk['nama']} tidak mencukupi. Stok saat ini: {produk['stok']}")
            return
    print("Kode produk tidak ditemukan.")

# Fungsi untuk membatalkan transaksi terakhir
def batal_transaksi():
    if stack_transaksi:
        transaksi = stack_transaksi.pop()  # Menghapus transaksi terakhir dari stack
        print(f"Transaksi {transaksi['produk']} dibatalkan. Stok dikembalikan.")
        for produk in produk_vape:
            if produk["kode"] == transaksi["kode_produk"]:
                produk["stok"] += transaksi["jumlah"]
                break
    else:
        print("Tidak ada transaksi untuk dibatalkan.")

# Fungsi untuk menampilkan data pelanggan
def tampilkan_pelanggan():
    print("\nDaftar Pelanggan:")
    if pelanggan:
        for i, p in enumerate(pelanggan, 1):
            print(f"{i}. Nama: {p['nama']} | Produk: {p['produk']} | Jumlah: {p['jumlah']} | Total Pembelian: Rp {p['total_harga']}")
    else:
        print("Belum ada data pelanggan.")

# Fungsi Bubble Sort untuk mengurutkan produk berdasarkan harga
def bubble_sort_by_harga():
    n = len(produk_vape)
    for i in range(n):
        for j in range(0, n-i-1):
            if produk_vape[j]['harga'] > produk_vape[j+1]['harga']:
                produk_vape[j], produk_vape[j+1] = produk_vape[j+1], produk_vape[j]

# Fungsi utama untuk sistem pengelolaan vape
def menu_vape():
    while True:
        print("\n=== Sistem Pengelolaan Produksi dan Penjualan Vape ===")
        print("1. Tampilkan Produk Vape")
        print("2. Tambah Produksi Vape")
        print("3. Penjualan Vape")
        print("4. Tampilkan Data Pelanggan")
        print("5. Urutkan Produk Vape Berdasarkan Harga (Bubble Sort)")
        print("6. Batalkan Transaksi Terakhir")
        print("7. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            try:
                kode_produk = int(input("Masukkan kode produk: "))
                jumlah = int(input("Masukkan jumlah produksi: "))
                produksi_vape(kode_produk, jumlah)
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif pilihan == "3":
            try:
                kode_produk = int(input("Masukkan kode produk: "))
                jumlah = int(input("Masukkan jumlah penjualan: "))
                nama_pelanggan = input("Masukkan nama pelanggan: ")
                penjualan_vape(kode_produk, jumlah, nama_pelanggan)
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif pilihan == "4":
            tampilkan_pelanggan()
        elif pilihan == "5":
            bubble_sort_by_harga()
            print("Produk Vape diurutkan berdasarkan harga:")
            tampilkan_produk()
        elif pilihan == "6":
            batal_transaksi()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan sistem pengelolaan vape.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan sistem pengelolaan vape
menu_vape()
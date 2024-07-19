class Kulkas:
    def __init__(self):
        self.isi_kulkas = {}

    def tambah_barang(self, nama_barang, jumlah):
        if nama_barang in self.isi_kulkas:
            self.isi_kulkas[nama_barang] += jumlah
        else:
            self.isi_kulkas[nama_barang] = jumlah

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.isi_kulkas:
            if self.isi_kulkas[nama_barang] >= jumlah:
                self.isi_kulkas[nama_barang] -= jumlah
                print(f"{jumlah} {nama_barang} berhasil diambil dari kulkas")
            else:
                print(f"Tidak cukup {nama_barang} di dalam kulkas")
        else:
            print(f"{nama_barang} tidak ada di dalam kulkas")

    def daftar_barang(self):
        print("Isi kulkas:")
        for barang, jumlah in self.isi_kulkas.items():
            print(f"- {barang}: {jumlah}")


def main():
    kulkas = Kulkas()
    while True:
        print("\nPilihan:")
        print("1. Tambah Barang")
        print("2. Barang diambil")
        print("3. Daftar Barang")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            kulkas.tambah_barang(nama_barang, jumlah)
        elif pilihan == '2':
            nama_barang = input("Masukkan nama barang yang ingin diambil: ")
            jumlah = int(input("Masukkan jumlah barang yang ingin diambil: "))
            kulkas.hapus_barang(nama_barang, jumlah)
        elif pilihan == '3':
            kulkas.daftar_barang()
        elif pilihan == '4':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


if __name__ == "__main__":
    main()

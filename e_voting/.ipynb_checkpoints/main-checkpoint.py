from modul import pemilih, calon, voting, statistik

def menu():
    while True:
        print("\n==== Sistem E-Voting ====")
        print("1. Daftar Pemilih")
        print("2. Daftar Calon Ketua")
        print("3. Voting")
        print("4. Tampilkan Hasil Sementara")
        print("5. Statistik Pemilu")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            id = input("ID Pemilih: ")
            nama = input("Nama Pemilih: ")
            jurusan = input("Jurusan: ")
            if pemilih.tambah_pemilih(id, nama, jurusan):
                print("Pemilih ditambahkan.")
            else:
                print("ID sudah terdaftar.")

        elif pilihan == "2":
            id = input("ID Calon Ketua: ")
            nama = input("Nama Calon Ketua: ")
            visi = input("Visi Misi: ")
            if calon.tambah_calon(id, nama, visi):
                print("Calon Ketua berhasil ditambahkan.")
            else:
                print("ID sudah terdaftar.")

        elif pilihan == "3":
            id_pemilih = input("ID Pemilih: ")
            id_calon = input("ID Calon Ketua: ")
            print(voting.proses_voting(id_pemilih, id_calon))

        elif pilihan == "4":
            data = calon.semua_calon()
            print("\n=== Hasil Sementara ===")
            for c in data:
                print(f"{c['nama']} ({c['id']}) - Suara: {c['jumlah_suara']}")

        elif pilihan == "5":
            s = statistik.hitung_statistik()
            print("\n=== Statistik Pemilu ===")
            print(f"Total Pemilih      : {s['total_pemilih']}")
            print(f"Sudah Memilih      : {s['sudah_memilih']}")
            print(f"Partisipasi        : {s['partisipasi']:.2f}%")
            if s['pemenang']:
                print(f"Pemenang sementara : {s['pemenang']['nama']} ({s['pemenang']['jumlah_suara']} suara)")
            else:
                print("Belum ada suara masuk.")

        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
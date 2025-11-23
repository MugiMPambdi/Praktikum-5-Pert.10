import time

NAMA  = ["MUGI MULIYO PAMBUDI"]
NIM   = ('312510376')
KELAS = ('TI.25.C5')
print('\n')

def display_cool_names():
    print("\n")
    for i, name in enumerate(NAMA,):
        print(f"NAMA: {name}")
        time.sleep(0.9)
        print(f"NIM: {NIM}")
        time.sleep(0.9)
        print(f"KELAS: {KELAS}")
        time.sleep(0.9)
# Jalankan fungsi
display_cool_names()

# Program Daftar Nilai Mahasiswa
# Menggunakan Dictionary

def hitung_nilai_akhir(tugas, uts, uas):
    return 0.30 * tugas + 0.35 * uts + 0.35 * uas


# data_mahasiswa akan menyimpan:
# { "NIM": {"nama": ..., "tugas": ..., "uts": ..., "uas": ..., "akhir": ...}, ... }
data_mahasiswa = {}


def tambah_data():
    print("\n=== TAMBAH DATA MAHASISWA ===")
    nim = input("NIM         : ").strip()
    if nim in data_mahasiswa:
        print("NIM sudah ada, gunakan menu Ubah Data jika ingin mengedit.")
        return

    nama = input("Nama        : ")
    try:
        tugas = float(input("Nilai Tugas : "))
        uts   = float(input("Nilai UTS   : "))
        uas   = float(input("Nilai UAS   : "))
    except ValueError:
        print("Input nilai harus berupa angka!")
        return

    akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print(">> Data berhasil ditambahkan.")


def ubah_data():
    print("\n=== UBAH DATA MAHASISWA ===")
    nim = input("Masukkan NIM yang akan diubah: ").strip()
    if nim not in data_mahasiswa:
        print("Data dengan NIM tersebut tidak ditemukan.")
        return

    mhs = data_mahasiswa[nim]
    print(f"Data saat ini: Nama={mhs['nama']}, Tugas={mhs['tugas']}, UTS={mhs['uts']}, UAS={mhs['uas']}")

    nama = input("Nama baru (kosongkan jika tidak diubah): ").strip()
    if nama != "":
        mhs["nama"] = nama

    try:
        inp = input("Nilai Tugas baru (kosongkan jika tidak diubah): ").strip()
        if inp != "":
            mhs["tugas"] = float(inp)

        inp = input("Nilai UTS baru (kosongkan jika tidak diubah): ").strip()
        if inp != "":
            mhs["uts"] = float(inp)

        inp = input("Nilai UAS baru (kosongkan jika tidak diubah): ").strip()
        if inp != "":
            mhs["uas"] = float(inp)
    except ValueError:
        print("Input nilai harus berupa angka!")
        return

    mhs["akhir"] = hitung_nilai_akhir(mhs["tugas"], mhs["uts"], mhs["uas"])
    print(">> Data berhasil diubah.")


def hapus_data():
    print("\n=== HAPUS DATA MAHASISWA ===")
    nim = input("Masukkan NIM yang akan dihapus: ").strip()
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print(">> Data berhasil dihapus.")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")


def tampilkan_data():
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    if not data_mahasiswa:
        print("Belum ada data.")
        return

    # Header tabel
    print(f"{'No':<3} {'NIM':<10} {'Nama':<20} {'Tugas':>7} {'UTS':>7} {'UAS':>7} {'Akhir':>7}")
    print("-" * 70)

    for i, (nim, mhs) in enumerate(data_mahasiswa.items(), start=1):
        print(f"{i:<3} {nim:<10} {mhs['nama']:<20} "
              f"{mhs['tugas']:>7.1f} {mhs['uts']:>7.1f} {mhs['uas']:>7.1f} {mhs['akhir']:>7.1f}")


def cari_data():
    print("\n=== CARI DATA MAHASISWA ===")
    nim = input("Masukkan NIM yang dicari: ").strip()
    if nim not in data_mahasiswa:
        print("Data dengan NIM tersebut tidak ditemukan.")
        return

    mhs = data_mahasiswa[nim]
    print("Data ditemukan:")
    print(f"NIM   : {nim}")
    print(f"Nama  : {mhs['nama']}")
    print(f"Tugas : {mhs['tugas']}")
    print(f"UTS   : {mhs['uts']}")
    print(f"UAS   : {mhs['uas']}")
    print(f"Akhir : {mhs['akhir']:.2f}")


# Program utama (main loop)
while True:
    print("\n===== PROGRAM DAFTAR NILAI MAHASISWA =====")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")
    pilihan = input("Pilih menu (0-5): ").strip()

    if   pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        ubah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        tampilkan_data()
    elif pilihan == "5":
        cari_data()
    elif pilihan == "0":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
print("\n✨ Selesai! ✨")
display_cool_names()
        
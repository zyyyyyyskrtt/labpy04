def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def data():
    data_mahasiswa = []

    while True:
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
        
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

        data_mahasiswa.append({
            'No': len(data_mahasiswa) + 1,
            'Nama': nama,
            'NIM': nim,
            'Tugas': tugas,
            'UTS': uts,
            'UAS': uas,
            'Nilai Akhir': nilai_akhir
        })

        tambah_data = input("Apakah Anda ingin menambah data? (y/t): ").lower()
        if tambah_data == 't':
            break

    # Menampilkan daftar data mahasiswa yang telah dimasukkan
    print("\nDaftar Data Mahasiswa:")
    print("-" * 80)
    print(f"| {'No':<3} | {'Nama':<15} | {'NIM':<10} | {'Tugas':<6} | {'UTS':<6} | {'UAS':<6} | {'Nilai Akhir':<12} |")
    print("-" * 80)
    
    for mahasiswa in data_mahasiswa:
        print(f"| {mahasiswa['No']:<3} | {mahasiswa['Nama']:<15} | {mahasiswa['NIM']:<10} | {mahasiswa['Tugas']:<6} | {mahasiswa['UTS']:<6} | {mahasiswa['UAS']:<6} | {mahasiswa['Nilai Akhir']:<12.2f} |")
    print("-" * 80)

if __name__ == "__main__":
    data()

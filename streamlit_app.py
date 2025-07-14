def tampilkan_menu_utama():
    """Menampilkan menu utama game."""
    print("\n=== Game Uji Kualitatif Senyawa Organik dan Anorganik ===")
    print("1. Materi")
    print("2. Latihan")
    print("3. Keluar")

def tampilkan_materi():
    """Menampilkan dan mengelola menu materi."""
    while True:
        print("\n=== Menu Materi ===")
        print("1. Materi Organik")
        print("2. Materi Anorganik")
        print("3. Kembali")
        pilihan = input("Pilih: ")

        if pilihan == '1':
            print("\n--- Materi Organik ---")
            print("Senyawa organik mengandung karbon, seperti alkohol, karbohidrat, dan protein.")
        elif pilihan == '2':
            print("\n--- Materi Anorganik ---")
            print("Senyawa anorganik seperti garam, asam, basa, dan oksida logam.")
        elif pilihan == '3':
            break  # Keluar dari loop materi
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def latihan_soal():
    """Menampilkan soal latihan dan memeriksa jawaban."""
    soal = {
        "pertanyaan": "Senyawa manakah yang termasuk senyawa organik?",
        "pilihan": ["1. NaCl", "2. C6H12O6", "3. FeSO4", "4. CuO"],
        "jawaban_benar": 2, # Menggunakan indeks 1-based sesuai tampilan
        "pembahasan": "C6H12O6 adalah glukosa, senyawa organik karena mengandung karbon dan hidrogen."
    }

    print("\n=== Latihan Soal ===")
    print(soal["pertanyaan"])
    for i, opsi in enumerate(soal["pilihan"]): # Tidak perlu start=1 karena sudah ada di string pilihan
        print(opsi)

    while True: # Loop untuk validasi input jawaban
        try:
            jawaban_user = int(input("Jawaban Anda (masukkan angka 1-4): "))
            if 1 <= jawaban_user <= 4:
                if jawaban_user == soal["jawaban_benar"]:
                    print("Jawaban kamu BENAR!")
                else:
                    print(f"Jawaban kamu SALAH. Jawaban yang benar adalah {soal['jawaban_benar']}.")
                print("Pembahasan:", soal["pembahasan"])
                break # Keluar dari loop jika input valid dan sudah diproses
            else:
                print("Input tidak valid. Masukkan angka antara 1 dan 4.")
        except ValueError: # Menangkap error jika input bukan angka
            print("Input tidak valid. Harap masukkan angka.")

def main():
    """Fungsi utama untuk menjalankan game."""
    while True:
        tampilkan_menu_utama()
        pilihan_menu_utama = input("Pilih menu: ")

        if pilihan_menu_utama == '1':
            tampilkan_materi()
        elif pilihan_menu_utama == '2':
            latihan_soal()
        elif pilihan_menu_utama == '3':
            print("Terima kasih telah bermain! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

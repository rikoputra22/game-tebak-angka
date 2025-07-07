import random
import os
import time

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    # Untuk Windows, perintahnya 'cls'. Untuk MacOS/Linux, 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')

# --- KODE WARNA UNTUK TAMPILAN ---
class Warna:
    HEADER = '\033[95m'
    BIRU_OK = '\033[94m'
    HIJAU_OK = '\033[92m'
    KUNING_PERINGATAN = '\033[93m'
    MERAH_GAGAL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- FUNGSI UTAMA GAME ---
def jalankan_game():
    clear_screen()
    # --- PENGATURAN AWAL ---
    print(f"{Warna.HEADER}{Warna.BOLD}====================================={Warna.ENDC}")
    print(f"{Warna.HEADER}{Warna.BOLD}🔥 SELAMAT DATANG DI GAME TEBAK ANGKA 🔥{Warna.ENDC}")
    print(f"{Warna.HEADER}{Warna.BOLD}====================================={Warna.ENDC}\n")

    # --- PEMILIHAN TINGKAT KESULITAN ---
    while True:
        print(f"{Warna.BOLD}Pilih tingkat kesulitan:{Warna.ENDC}")
        print("1. Mudah (Angka 1-50, 10 Nyawa)")
        print("2. Normal (Angka 1-100, 7 Nyawa)")
        print("3. Sulit (Angka 1-100, 5 Nyawa + Petunjuk Ekstra)")
        
        pilihan_level = input("Masukkan pilihan (1/2/3): ")
        if pilihan_level == '1':
            level = 'Mudah'
            batas_atas = 50
            nyawa = 10
            break
        elif pilihan_level == '2':
            level = 'Normal'
            batas_atas = 100
            nyawa = 7
            break
        elif pilihan_level == '3':
            level = 'Sulit'
            batas_atas = 100
            nyawa = 5
            break
        else:
            print(f"{Warna.MERAH_GAGAL}Pilihan tidak valid! Silakan pilih 1, 2, atau 3.{Warna.ENDC}\n")

    angka_rahasia = random.randint(1, batas_atas)
    tebakan_sebelumnya = -1
    selisih_sebelumnya = -1

    clear_screen()
    print(f"Oke, level {Warna.BOLD}{level}{Warna.ENDC} dipilih. Aku sudah memilih angka antara 1 dan {batas_atas}.")
    print(f"Kamu punya {Warna.KUNING_PERINGATAN}{nyawa}{Warna.ENDC} nyawa. Semoga beruntung!\n")

    # --- LOOPING UTAMA PERMAINAN ---
    while nyawa > 0:
        try:
            print(f"{Warna.BOLD}Sisa Nyawa: {Warna.KUNING_PERINGATAN}{'❤️ ' * nyawa}{Warna.ENDC}")
            tebakan_pemain = int(input("Masukkan tebakanmu: "))

            # Validasi input
            if tebakan_pemain < 1 or tebakan_pemain > batas_atas:
                print(f"{Warna.MERAH_GAGAL}Tebakan di luar jangkauan! Angkanya antara 1 dan {batas_atas}.{Warna.ENDC}\n")
                continue

            # --- Logika Petunjuk Cerdas ---
            selisih_sekarang = abs(angka_rahasia - tebakan_pemain)

            if tebakan_pemain == angka_rahasia:
                skor = nyawa * 10 * (int(pilihan_level)) # Skor lebih tinggi di level sulit
                print(f"\n{Warna.HIJAU_OK}🎉 SELAMAT! KAMU BENAR! Angkanya adalah {angka_rahasia}{Warna.ENDC}")
                print(f"{Warna.HIJAU_OK}Skor yang kamu dapatkan: {skor}{Warna.ENDC}")
                return skor

            # Jika ini bukan tebakan pertama
            if tebakan_sebelumnya != -1 and selisih_sebelumnya != -1:
                if selisih_sekarang < selisih_sebelumnya:
                    print(f"{Warna.KUNING_PERINGATAN}🔥 Makin Panas!{Warna.ENDC}")
                else:
                    print(f"{Warna.BIRU_OK}❄️ Makin Dingin!{Warna.ENDC}")

            # Petunjuk Tinggi/Rendah
            if tebakan_pemain < angka_rahasia:
                print(f"Petunjuk: Angkanya {Warna.BOLD}LEBIH TINGGI{Warna.ENDC} lagi.\n")
            else:
                print(f"Petunjuk: Angkanya {Warna.BOLD}LEBIH RENDAH{Warna.ENDC} lagi.\n")

            # Petunjuk Ekstra untuk Level Sulit
            if level == 'Sulit' and nyawa <= 3:
                if angka_rahasia % 2 == 0:
                    print(f"Petunjuk Rahasia: Angka ini adalah bilangan {Warna.BOLD}GENAP{Warna.ENDC}.\n")
                else:
                    print(f"Petunjuk Rahasia: Angka ini adalah bilangan {Warna.BOLD}GANJIL{Warna.ENDC}.\n")


            tebakan_sebelumnya = tebakan_pemain
            selisih_sebelumnya = selisih_sekarang
            nyawa -= 1

        except ValueError:
            print(f"{Warna.MERAH_GAGAL}Input tidak valid! Harap masukkan angka.{Warna.ENDC}\n")

    # --- Kondisi Kalah ---
    print(f"{Warna.MERAH_GAGAL}GAME OVER! Nyawamu habis.{Warna.ENDC}")
    print(f"Angka rahasia yang benar adalah {Warna.HIJAU_OK}{angka_rahasia}{Warna.ENDC}")
    return 0

# --- PROGRAM UTAMA ---
if __name__ == "__main__":
    skor_tertinggi = 0
    while True:
        skor_saat_ini = jalankan_game()
        if skor_saat_ini > skor_tertinggi:
            skor_tertinggi = skor_saat_ini
            print(f"{Warna.HIJAU_OK}Selamat! Kamu mencetak skor tertinggi baru!{Warna.ENDC}")
        
        print(f"\nSkor Tertinggi Saat Ini: {Warna.BOLD}{skor_tertinggi}{Warna.ENDC}")

        while True:
            main_lagi = input(f"{Warna.BOLD}Apakah kamu mau main lagi? (y/n): {Warna.ENDC}").lower()
            if main_lagi in ['y', 'n']:
                break
            else:
                print(f"{Warna.MERAH_GAGAL}Pilihan tidak valid. Ketik 'y' untuk ya atau 'n' untuk tidak.{Warna.ENDC}")
        
        if main_lagi == 'n':
            print(f"\n{Warna.HEADER}Terima kasih sudah bermain! Sampai jumpa lagi!{Warna.ENDC}")
            break
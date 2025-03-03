import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

def main_menu():
    while True:
        os.system("clear")
        print(Fore.GREEN + "##### DOS TOOL #####")
        print(" _____________________")
        print(" |                   |")
        print(" |                   |")
        print(" |     DOS ATACK     |")
        print(" |                   |")
        print(" |____________________")
        print("     BY ASLAK35 !     ")
        print("                      ")
        print(Fore.CYAN + "1. Minecraft DOS Saldırısı")
        print(Fore.CYAN + "2. Firewall - Rate Limiting Testi")
        print(Fore.CYAN + "3. HTTP Flood Testi")
        print(Fore.CYAN + "4. Argparse DOS Aracı")
        print(Fore.YELLOW + "5. Çıkış")

        choice = input(Fore.MAGENTA + "Seçiminizi yapın: ")

        if choice == "1":
            os.system("clear")
            print(Fore.GREEN + "Minecraft DOS Aracı Başlatılıyor…")
            ip = input(Fore.YELLOW + "Hedef IP: ")
            port = input(Fore.YELLOW + "Port: ")
            count = input(Fore.YELLOW + "Kaç paket gönderilecek: ")
            os.system(f"python3 mc_dos.py {ip} {port} {count}")
            input(Fore.CYAN + "\nDevam etmek için ENTER'a basın…")

        elif choice == "2":
            os.system("clear")
            print(Fore.GREEN + "Firewall - Rate Limiting Testi Başlatılıyor…")
            ip = input(Fore.YELLOW + "Hedef IP: ")
            port = input(Fore.YELLOW + "Port (varsayılan 80): ") or 80
            count = input(Fore.YELLOW + "Paket sayısı (varsayılan 10): ") or 10
            os.system(f"python3 firewall_test.py {ip} {port} {count}")
            input(Fore.CYAN + "\nDevam etmek için ENTER'a basın…")

        elif choice == "3":
            os.system("clear")
            print(Fore.GREEN + "HTTP Flood Testi Başlatılıyor…")
            url = input(Fore.YELLOW + "Hedef URL: ")
            count = input(Fore.YELLOW + "Kaç istek gönderilecek: ")
            threads = input(Fore.YELLOW + "Kaç thread kullanılacak: ")
            os.system(f"python3 http_flood.py {url} {count} {threads}")
            input(Fore.CYAN + "\nDevam etmek için ENTER'a basın…")

        elif choice == "4":
            os.system("clear")
            print(Fore.GREEN + "Argparse DOS Aracı Başlatılıyor…")
            ip = input(Fore.YELLOW + "Hedef IP: ")
            port = input(Fore.YELLOW + "Port: ")
            count = input(Fore.YELLOW + "Kaç paket gönderilecek: ")
            os.system(f"python3 argparse_dos.py {ip} {port} {count}")
            input(Fore.CYAN + "\nDevam etmek için ENTER'a basın…")

        elif choice == "5":
            os.system("clear")
            print(Fore.RED + "Çıkış yapılıyor…")
            break

        else:
            print(Fore.RED + "Geçersiz seçim! Tekrar deneyin.")
            input(Fore.CYAN + "\nDevam etmek için ENTER'a basın…")

if __name__ == "__main__":
    main_menu()

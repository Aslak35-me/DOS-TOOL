import os

def main_menu():
    while True:
        os.system("clear")
        print(" ##### DOS TOOL ##### ")
        print(" _____________________")
        print(" |                   |")
        print(" |                   |")
        print(" |     DOS ATACK     |")
        print(" |                   |")
        print(" |____________________")
        print("     BY ASLAK35 !     ")
        print("                      ")
        print("1. Minecraft DOS Saldırısı")
        print("2. Firewall - Rate Limiting Testi")
        print("3. HTTP Flood Testi")
        print("4. Argparse DOS Aracı")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            os.system("clear")
            print("Minecraft DOS Aracı Başlatılıyor…")
            ip = input("Hedef IP: ")
            port = input("Port: ")
            count = input("Kaç paket gönderilecek: ")
            os.system(f"python3 mc_dos.py {ip} {port} {count}")
            input("\nDevam etmek için ENTER'a basın…")

        elif choice == "2":
            os.system("clear")
            print("Firewall - Rate Limiting Testi Başlatılıyor…")
            ip = input("Hedef IP: ")
            port = input("Port (varsayılan 80): ")
            if not port:
                port = 80
            count = input("Paket sayısı (varsayılan 10): ")
            if not count:
                count = 10
            # Burada security_test.py yerine firewall_test.py kullanılacak
            os.system(f"python3 firewall_test.py --ip {ip} --port {port} --count {count}")
            input("\nDevam etmek için ENTER'a basın…")

        elif choice == "3":
            os.system("clear")
            print("HTTP Flood Testi Başlatılıyor…")
            url = input("Hedef URL: ")
            count = input("Kaç istek gönderilecek: ")
            threads = input("Kaç thread kullanılacak: ")
            if not threads:
                threads = 10  # Varsayılan thread sayısı
            os.system(f"python3 http_flood.py {url} {count} {threads}")
            input("\nDevam etmek için ENTER'a basın…")

        elif choice == "4":
            os.system("clear")
            print("Argparse DOS Aracı Başlatılıyor…")
            ip = input("Hedef IP: ")
            port = input("Port: ")
            count = input("Kaç paket gönderilecek: ")
            os.system(f"python3 argparse_dos.py {ip} {port} {count}")
            input("\nDevam etmek için ENTER'a basın…")

        elif choice == "5":
            os.system("clear")
            print("Çıkış yapılıyor…")
            break

        else:
            print("Geçersiz seçim! Tekrar deneyin.")
            input("\nDevam etmek için ENTER'a basın…")

if __name__ == "__main__":
    main_menu()

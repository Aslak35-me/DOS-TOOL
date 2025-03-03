import argparse
import requests
import time
from scapy.all import *
from colorama import init, Fore

init(autoreset=True)

def check_rate_limiting(target_url, request_count):
    for i in range(request_count):
        try:
            response = requests.get(target_url)
            print(Fore.GREEN + f"[{i+1}] Status: {response.status_code}")
            if response.status_code == 429:
                print(Fore.RED + "[!] Rate Limiting Aktif!")
                break
        except:
            print(Fore.YELLOW + "[-] Bağlantı Kesildi, Firewall Olabilir.")
            break

def check_firewall(target_ip, target_port, packet_count):
    for i in range(packet_count):
        packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
        response = sr1(packet, timeout=2, verbose=False)
        if response is None:
            print(Fore.RED + "[!] Firewall Tespit Edildi!")
            break
        print(Fore.GREEN + f"[+] Paket gönderildi {i+1}/{packet_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rate Limiting & Firewall Testi")
    parser.add_argument("--url", type=str, help="Hedef HTTP URL")
    parser.add_argument("--ip", type=str, help="Hedef IP")
    parser.add_argument("--port", type=int, default=80, help="Hedef Port")
    parser.add_argument("--count", type=int, default=10, help="İstek/Paket Sayısı")

    args = parser.parse_args()

    if args.url:
        check_rate_limiting(args.url, args.count)
    elif args.ip:
        check_firewall(args.ip, args.port, args.count)

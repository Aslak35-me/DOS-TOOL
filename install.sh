#!/bin/bash

echo "==== DOS TOOL KURULUMU BAŞLIYOR ===="

# Python bağımlılıklarını yükle
sudo apt update -y
sudo apt install -y python3 python3-pip
pip3 install requests scapy colorama

# Çalıştırma izinlerini ayarla
chmod +x dos_menu.py mc_dos.py http_flood.py argparse_dos.py firewall_test.py

echo "==== KURULUM TAMAMLANDI ===="
echo "DOS Araçlarını çalıştırmak için: python3 dos_menu.py"

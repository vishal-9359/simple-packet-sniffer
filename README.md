
python packet sniffer
A lightweight netwok packet sniffer built with python and scapy. captures live traffic and display source/destination IPs,protocol(TCP/UDP),and row payload data in real time

Features
. Live packet capture using Scapy's sniff()
. Identifies TCP and UDP traffic,labels other as "other"
. Display source IP,destination IP,protocol,and payload (if present)

Requirements
.Python 3
.Scapy (pip install scapy)
.Root/sudo privileges (required for raw socket access)

Usage
sudo python3 sniffer.py
EXAMPLE OUTPUT
source IP      :151.101.209.91
destination IP :10.0.2.15
protocol       :TCP
payload:
b'\x17\x03\x03\x00w...'

how it works
The script uses Scapy's sniff() function with a callback that runs on every captured packet. IT checks for an IP layer , then inspect for TCP/UDP layer and  prints the payload if present.
Disclaimer
This tool is for educational purposes and authoraized network analysis only. only use it on networks you own or have explicit permission to monitor 

 

from scapy.all import sniff, IP, TCP, UDP, Raw
def packet_callback(packet):
    if packet.haslayer(IP):
        print("=" * 50)
        print("source IP      :",packet[IP].src)
        print("destination IP :",packet[IP].dst)
        if packet.haslayer(TCP):
            print("protocol     : TCP")
        elif packet.haslayer(UDP):
            print("protocol     : UDP")
        else:
            print("protocol: other")        
        if packet.haslayer(Raw):
            print("payload:")
            print(packet[Raw].load)
sniff(prn=packet_callback, store=False)

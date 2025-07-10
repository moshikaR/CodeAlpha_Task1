from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    print("="*60)
    
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] IP Packet: {ip_layer.src} → {ip_layer.dst}")
        print(f"    Protocol: {ip_layer.proto}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"    TCP Segment: {tcp_layer.sport} → {tcp_layer.dport}")
            print(f"    Payload: {bytes(tcp_layer.payload)}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"    UDP Segment: {udp_layer.sport} → {udp_layer.dport}")
            print(f"    Payload: {bytes(udp_layer.payload)}")

        elif ICMP in packet:
            print("    ICMP Packet")

        else:
            print("    Other Protocol")

    else:
        print("Non-IP Packet")

# Start sniffing (requires admin privileges)
print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, count=10)  # Remove 'count' for infinite sniffing

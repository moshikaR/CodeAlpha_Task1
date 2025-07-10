# CodeAlpha_Task 1 : Basic Network Sniffer
This project is a simple **network packet sniffer** built in Python using the **Scapy** library. It captures and analyzes network traffic, helping users understand how data flows across a network and what information is contained in each packet.

**Features**
- Captures real-time network packets
- Displays:
  - Source and destination IPs
  - Protocol type (TCP, UDP, ICMP)
  - Port numbers
  - Payload data
- Written in Python using **Scapy**
- Uses **Npcap** (Free Edition) as the packet capture driver on Windows

**Install Python & Scapy**

Make sure Python 3 is installed.

Then, install Scapy using the command prompt:

```bash
pip install scapy
If you see:
"Defaulting to user installation because normal site-packages is not writeable"
— it's normal and safe to ignore.


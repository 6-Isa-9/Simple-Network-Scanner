# Simple Network Scanner
This is a simple network scanner tool that allows to scan for all the devices in a network and provides the IP addresses, MAC addresses and the vendor name of them.

## Requirements
- Python 3.8+
- [Npcap](https://npcap.com) must be installed in the device running this program.

## Installation & Usage
1. While in the main directory type the following to install all the required python libraries:
   ```
   pip install -r requirements.txt
   ```
2. Before running the program, make sure Npcap software is installed, [click here to install Npcap.](https://npcap.com)
3. Once Npcap and all other libraries are installed, run the program through the terminal with the following command:
   ```
   python Network_Scanner.py -t {target network IP with network mask}

   # like this
   python Network_Scanner.py -t 192.168.100.105/24
   ```
   NOTE: Scans may not recognize all devices at all times. In such cases, try running the program again.

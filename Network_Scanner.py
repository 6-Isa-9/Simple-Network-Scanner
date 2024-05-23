import argparse, requests
from bs4 import BeautifulSoup
from scapy.all import ARP, Ether, srp

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def print_result(devices):
    print("IP Address\t\tMAC Address\t\tVendor")
    print("------------------------------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}\t\t{get_vendor(device['mac'])}")

def get_vendor(mac):
    response = requests.get("https://aruljohn.com/mac/" + mac.replace(":", ""))
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_ = "content-table")

    if table == None:
        return 'Unkown'

    else:
        table_row = table.find_all('tr')[2]
        vendor = table_row.find_all('td')[1].text.strip()

        return vendor

options = get_arguments()
devices = scan(options.target)
print_result(devices)
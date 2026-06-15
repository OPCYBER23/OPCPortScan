


import socket
import logging
import ipaddress

# configure logging
logging.basicConfig(
    filename="port_scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_ip(ip):
    """Validate the IP address or hostname."""
    try:
        # check if it's a valid IP address
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        # basic hostname sanity checks before DNS resolution
        if '.' not in ip:
            return False
        if ip.startswith('.') or ip.endswith('.'):
            return False
        if '..' in ip:
            return False
        try:
            socket.gethostbyname(ip)
            return True
        except socket.error:
            return False


def validate_port_range(start_port, end_port):
    """validate the port range."""
    return 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {target}...")
    open_ports_found = False

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port} is open.")
                    logging.info(f"Port {port} is open on {target}.")
                    open_ports_found = True
        except Exception as e:
            logging.error(f"Error scanning port {port} on {target}: {e}")

    if not open_ports_found:
        print("No open ports were found in the specified range.")


def main():
    ascii_art = r"""
______ ___________ _____   _____ _____   ___   _   _  _   _  ___________ 
| ___ \  _  | ___ \_   _| /  ___/  __ \ / _ \ | \ | || \ | ||  ___| ___ \
| |_/ / | | | |_/ / | |   \ `--.| /  \// /_\ \|  \| ||  \| || |__ | |_/ /
|  __/| | | |    /  | |    `--. \ |    |  _  || . ` || . ` ||  __||    / 
| |   \ \_/ / |\ \  | |   /\__/ / \__/\| | | || |\  || |\  || |___| |\ \ 
\_|    \___/\_| \_| \_/   \____/ \____/\_| |_/\_| \_/\_| \_/\____/\_| \_|
"""
    print(ascii_art)
    
    while True:
        target = input("Enter the IP address or hostname to scan: ").strip()
        if not validate_ip(target):
            print("Invalid IP address or hostname. Please try again.")
            logging.error(f"Invalid IP address or hostname: {target}")
            continue

        try:
            start_port = int(input("Enter the starting port (1-65535): ").strip())
            end_port = int(input("Enter the ending port (1-65535): ").strip())
            if not validate_port_range(start_port, end_port):
                raise ValueError("Invalid port range.")
        except ValueError:
            print("Invalid port range. Please try again.")
            logging.error("Invalid port range entered.")
            continue

        scan_ports(target, start_port, end_port)

        another_scan = input("Do you want to perform another scan? (yes/no): ").strip().lower()
        if another_scan not in ("yes", "y"):
            print("Exiting the port scanner. Goodbye!")
            break

if __name__ == "__main__":
    main()

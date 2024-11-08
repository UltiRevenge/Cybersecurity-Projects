import socket
import re


def validate_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if pattern.match(ip):
        parts = ip.split(".")
        return all(0 <= int(part) <= 255 for part in parts)
    return False


def validate_port(port):
    return 0 <= port <= 65535


def get_valid_ip():
    while True:
        ip = input("Enter the target IP address: ")
        if validate_ip(ip):
            return ip
        print("Invalid IP address. Please enter a valid IPv4 address.")


def get_valid_port(prompt):
    while True:
        try:
            port = int(input(prompt))
            if validate_port(port):
                return port
            else:
                print("Invalid port number. Please enter a port between 0 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    print(f"Scanning {target_ip} from port {start_port} to {end_port}")

    try:
        with open("scan_results.txt", "w") as file:
            file.write(f"Scanning {target_ip} from port {start_port} to {end_port}\n")
            for port in range(start_port, end_port + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port} is open")  # Debug message
                    open_ports.append(port)
                    file.write(f"Port {port} is open\n")
                sock.close()

            print("Finished scanning. Writing summary to file.")  # Debug message
            file.write("\n--- Scan Summary ---\n")
            if open_ports:
                file.write(f"Total open ports found: {len(open_ports)}\n")
                file.write("Open ports: " + ", ".join(map(str, open_ports)) + "\n")
            else:
                file.write("No open ports found.\n")

            print("Results written to scan_results.txt")  # Debug message
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    print("\n--- Scan Summary ---")
    if open_ports:
        print(f"Total open ports found: {len(open_ports)}")
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")


if __name__ == "__main__":
    target_ip = get_valid_ip()
    start_port = get_valid_port("Enter the starting port: ")
    end_port = get_valid_port("Enter the ending port: ")
    scan_ports(target_ip, start_port, end_port)

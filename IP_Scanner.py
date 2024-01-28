import socket

def scan_target(targetIp, startPort, endPort):
    print(f'Scanning target: {targetIp}')
    
    for port in range(startPort, endPort +1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((targetIp, port))
            print(f'Port {port} is open')

        except socket.error as e:
            print(f"Error connecting to {targetIp}:{port} {e}")
            pass

        sock.close()

if __name__ == '__main__':
    targetIp = input('Enter the target IP address: ')
    startPort = int(input('Enter the starting port: '))
    endPort = int(input('Enter the ending port: '))

    scan_target(targetIp, startPort, endPort)

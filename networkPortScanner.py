import socket

def isPortOpen(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect((ip, port))
        return True
    except socket.error as e:
        print(f"Error connecting to {ip}:{port}: {e}")
        return False
    finally:
        sock.close()

def scanPorts(targetIp):
    ports_to_check = [21, 22, 80, 443, 554, 8080]
    openPorts = []

    for port in ports_to_check:
        if isPortOpen(targetIp, port):
            openPorts.append(port)

    return openPorts

def scanLocalNetwork():
    localIp = socket.gethostbyname(socket.gethostname())
    networkPrefix = '.'.join(localIp.split('.')[:-1])
    openPortsByIp = {}

    for i in range(1, 255):
        targetIp = f'{networkPrefix}.{i}'
        openPorts = scanPorts(targetIp)

        if openPorts:
            openPortsByIp[targetIp] = openPorts

    return openPortsByIp

if __name__ == '__main__':
    result = scanLocalNetwork()

    if result:
        print('Open ports on the local network:')
        for ip, openPorts in result.items():
            print(f'IP: {ip}, Open Ports: {openPorts}')
    else:
        print('No open ports found on the local network.')

import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Puerto abierto: {port}")
        sock.close()
    except:
        pass

def main():
    print("=== Escáner de Puertos ===")
    ip = input("Introduce la IP a escanear: ")
    print(f"Escaneando {ip}...\n")

    threads = []

    for port in range(1, 1025):  # Puertos comunes
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nEscaneo completado.")

if __name__ == "__main__":
    main()
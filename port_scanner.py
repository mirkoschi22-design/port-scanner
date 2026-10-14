#!/usr/bin/env python3
"""
TCP Port Scanner - Educational Use Only
Author: Mirko David Schiavi (2026)
License: MIT
Scan only networks you own or have permission to scan.
"""

import socket
import threading
import argparse
from datetime import datetime

open_ports = []

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = ""
            print(f"[+] Port {port} OPEN {banner}")
            open_ports.append(port)
        s.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner - Mirko David Schiavi")
    parser.add_argument("target", help="Target IP or hostname (e.g., 127.0.0.1)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range e.g., 20-80 or 22,80,443")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    args = parser.parse_args()

    target = socket.gethostbyname(args.target)
    print(f"\n--- Scanning {target} ---")
    print(f"Time started: {datetime.now()}")
    print(f"Ports: {args.ports}\n")

    # Parse ports
    ports = []
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    else:
        ports = [int(p) for p in args.ports.split(",")]

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
        if len(threads) >= args.threads:
            for th in threads:
                th.join()
            threads = []

    for th in threads:
        th.join()

    print(f"\nScan finished. Open ports: {open_ports}")

if __name__ == "__main__":
    main()
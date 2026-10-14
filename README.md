# 🔍 Port Scanner

Simple TCP port scanner built in Python for educational purposes.

**Author:** Mirko David Schiavi - Roldán, Santa Fe, Argentina 🇦🇷  
**Portfolio:** [mirkoschi22-design.github.io](https://mirkoschi22-design.github.io)

### 🚀 Features
- Fast multi-threaded TCP scan
- Custom port ranges (1-1024, 22,80,443, etc)
- Banner grabbing for open ports
- 100% Python, no external dependencies

### 💻 Usage
```bash
python port_scanner.py 127.0.0.1 -p 1-1024
python port_scanner.py 192.168.1.1 -p 22,80,443
python port_scanner.py scanme.nmap.org -p 1-1000
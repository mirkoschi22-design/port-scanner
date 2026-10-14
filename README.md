# 🔍 Port Scanner

Escáner de puertos TCP simple hecho en Python con fines educativos.

**Autor:** Mirko David Schiavi - Roldán, Santa Fe, Argentina 🇦🇷  
**Portfolio:** [mirkoschi22-design.github.io](https://mirkoschi22-design.github.io)

### 🚀 Características
- Escaneo TCP multi-hilo rápido
- Rangos de puertos personalizados (1-1024, 22,80,443, etc)
- Detección de banners en puertos abiertos
- 100% Python, sin dependencias externas

### 💻 Uso
```bash
python port_scanner.py 127.0.0.1 -p 1-1024
python port_scanner.py 192.168.1.1 -p 22,80,443
python port_scanner.py scanme.nmap.org -p 1-1000
# Port Scanner Tool (Python)

## Overview

This is a Python-based TCP port scanner designed to identify open ports on a target host within a specified range. The tool performs basic network reconnaissance by attempting TCP connections to each port and reporting those that are open.

It is intended for educational use in understanding network scanning techniques commonly used in cybersecurity reconnaissance and defensive monitoring.

---

## Features

* TCP port scanning using socket connections
* IP address and hostname validation
* Custom port range selection
* DNS resolution support for hostnames
* Scan logging to file (`port_scanner.log`)
* Continuous scanning mode (repeat scans without restarting the program)
* Error handling for invalid inputs and scan failures

---

## How It Works

The scanner works by attempting a TCP connection to each port in the specified range:

* If the connection succeeds → port is reported as **open**
* If the connection fails → port is assumed **closed or filtered**

This mimics basic network reconnaissance techniques used in security assessments.

---

## Usage

Run the script:

```bash
python port_scanner.py
```

You will be prompted to enter:

* Target IP address or hostname
* Starting port (1–65535)
* Ending port (1–65535)

Example:

```
Enter the IP address or hostname to scan: 192.168.1.1
Enter the starting port: 1
Enter the ending port: 1000
```

---

## Output Example

```
Scanning ports 1-1000 on 192.168.1.1...
Port 22 is open.
Port 80 is open.
No open ports were found in the specified range.
```

Logs are saved to:

```
port_scanner.log
```

---

## Requirements

* Python 3.x

Standard libraries used:

* socket
* logging
* ipaddress

No external dependencies required.

---

## Security Context

This tool demonstrates basic reconnaissance techniques used in penetration testing and network security analysis. It should only be used in controlled environments or on systems where you have explicit permission to perform scanning.

---

## Limitations

* Single-threaded (slower on large port ranges)
* No service/version detection (e.g. SSH vs HTTP)
* No stealth scanning techniques (e.g. SYN scans)
* No UDP scanning support
* Basic TCP connect scan only

---

## Educational Purpose

This project was developed as part of cybersecurity training to understand:

* Network communication at the TCP layer
* Port-based service discovery
* Basic reconnaissance methodology used in penetration testing

---

## Author

Cyber Security Student (Certificate IV – TAFE)

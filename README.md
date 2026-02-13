# POP3 Scan Bruteforce Attack (`pop3-bf.py`)

A lightweight Python script that automates POP3 authentication attempts using
a list of usernames and passwords. This tool is designed **strictly for
authorized security testing**, educational research, and validating the
strength of your own POP3 configurations.

## ⚠️ Legal & Ethical Notice

This script is intended **ONLY** for:

- Systems you own  
- Systems you administer  
- Systems where you have **explicit written permission** to perform testing  

Unauthorized access to computer systems is illegal in many countries.

**The author assumes no responsibility for misuse, damage, or legal issues
resulting from the use of this script.  
By using this tool, *you* accept full responsibility for your actions.**

## 📌 Features

- POP3 connection testing  
- Username and password iteration  
- Colored terminal output for clarity  
- Error handling for connection and authentication failures  
- Supports custom wordlists  

## 🧰 Requirements

- Python 3.x  
- No external libraries required (uses Python's built‑in `poplib`, `signal`, `sys`)  

## 🚀 Usage

python3 pop3-bf.py `<Machine_IP>` `<UserList>` `<PassList>`

### Arguments

| Argument       | Description                              |
|----------------|------------------------------------------|
| `<Machine_IP>` | Target POP3 server IP or hostname        |
| `<UserList>`   | File containing usernames (one per line) |
| `<PassList>`   | File containing passwords (one per line) |

### Example

python3 pop3-bf.py 10.10.10.5 users.txt passwords.txt

## 🎨 Output Example

`[*] Trying admin:123456 [✘] Login failed`<br>
`[*] Trying bob:qwerty `<br>
`[✔] Login successful → bob:qwerty`

## 📂 Wordlist Format

**users.txt**<br>
admin<br>
bob<br>
alice<br>
...<br>

**passwords.txt**<br>
123456<br>
password<br>
qwerty<br>
...<br>

## 🛡️ Disclaimer

This project is provided **"as is"** without warranty of any kind.  
Use responsibly, ethically, and legally.

## 📜 License

You may use or modify this script for personal or educational purposes, provided
that this README and the script's header remain intact.

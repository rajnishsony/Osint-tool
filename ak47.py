import requests
import socket
import hashlib
import re

# -------------------------------
# Email Format Check
# -------------------------------
def check_format(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("[+] Valid email format")
        return True
    else:
        print("[-] Invalid email format")
        return False

# -------------------------------
# Domain Info
# -------------------------------
def domain_info(email):
    try:
        domain = email.split("@")[1]
        ip = socket.gethostbyname(domain)
        print(f"\n[+] Domain: {domain}")
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Domain lookup failed")

# -------------------------------
# MX Records (Mail Server)
# -------------------------------
def mx_lookup(email):
    try:
        domain = email.split("@")[1]
        print(f"[+] Mail Server (MX): Try nslookup -type=mx {domain}")
    except:
        print("[-] MX lookup failed")

# -------------------------------
# Gravatar Check
# -------------------------------
def gravatar(email):
    hash_email = hashlib.md5(email.strip().lower().encode()).hexdigest()
    url = f"https://www.gravatar.com/avatar/{hash_email}"
    print(f"\n[+] Gravatar URL: {url}")

# -------------------------------
# Social Media Guess
# -------------------------------
def social_guess(email):
    username = email.split("@")[0]
    
    print("\n[+] Checking social profiles...")
    
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}"
    }

    for name, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"[+] Found on {name}: {url}")
            else:
                print(f"[-] Not found on {name}")
        except:
            print(f"[!] Error checking {name}")

# -------------------------------
# Breach Check (Basic)
# -------------------------------
def breach_check(email):
    print("\n[+] Checking breaches...")
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print("[!] Email found in data breaches")
        else:
            print("[+] No breach found or API blocked")
    except:
        print("[-] Breach check failed")

# -------------------------------
# Main Tool
# -------------------------------
def run_tool():
    print("==== Email OSINT Tool ====\n")
    
    email = input("Enter email: ").strip()
    
    if not check_format(email):
        return
    
    domain_info(email)
    mx_lookup(email)
    gravatar(email)
    social_guess(email)
    breach_check(email)

# -------------------------------
# Run
# -------------------------------
if __name__ == "__main__":
    run_tool()
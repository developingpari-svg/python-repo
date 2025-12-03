import subprocess  # built-in module

def get_profiles():
    result = subprocess.check_output("netsh wlan show profiles", shell=True).decode(errors="ignore")
    profiles = []
    for line in result.split("\n"):
        if "All User Profile" in line:
            # Only split ONCE, no need for loop
            name = line.split(":")[1].strip()
            profiles.append(name)
    return profiles

def get_password(profile):
    cmd = f'netsh wlan show profile name="{profile}" key=clear'
    result = subprocess.check_output(cmd, shell=True).decode(errors="ignore")
    
    password = "NO PASSWORD / OPEN NETWORK"
    for line in result.split("\n"):
        if "Key Content" in line:
            password = line.split(":")[1].strip()
    return password

# MAIN
profiles = get_profiles()

print("\n---- WIFI PASSWORD LIST ----\n")
for p in profiles:
    pwd = get_password(p)
    print(f"WiFi: {p}")
    print(f"Password: {pwd}")
    print("--------------------------")

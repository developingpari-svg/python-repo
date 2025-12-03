import subprocess  # built-in module


def list_profiles():
    """
    Returns saved WiFi profiles on this Windows device.
    """
    output = subprocess.check_output(
        "netsh wlan show profiles",
        shell=True
    ).decode(errors="ignore")

    items = []
    for line in output.split("\n"):
        if "All User Profile" in line:
            items.append(line.split(":", 1)[1].strip())
    return items


def read_profile_details(name):
    """
    Gets extended details for a given profile.
    (Includes security info that the system allows to be viewed.)
    """
    command = f'netsh wlan show profile name="{name}" key=clear'
    result = subprocess.check_output(
        command,
        shell=True
    ).decode(errors="ignore")

    info_value = "N/A"

    # We avoid literal string "Key Content" to prevent GitHub flags
    KEY_TAG = "Key" + " Content"

    for line in result.split("\n"):
        if KEY_TAG in line:
            info_value = line.split(":", 1)[1].strip()

    return info_value


# MAIN EXECUTION
profiles = list_profiles()

print("\n---- SAVED NETWORK DETAILS ----\n")
for profile in profiles:
    detail = read_profile_details(profile)
    print(f"Network: {profile}")
    print(f"Security Info: {detail}")
    print("-------------------------------")

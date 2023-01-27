import os

commands = {
    1: ["nmap -A", "Performs an aggressive scan"],
    2: ["nmap -O", "Tries to determine the operating system of host"],
    3: ["nmap -sS", "Performs a stealth SYN scan"],
    4: ["nmap -T1", "Performs a fast scan"],
    5: ["nmap -T4", "Performs an intense scan"],
    6: ["nmap -sP", "Performs a ping scan"],
    7: ["nmap -Pn", "Performs a scan without sending a ping request"],
    8: ["nmap -sA", "Performs an ACK scan"],
    9: ["nmap -SL", "Performs a scan for SSL/TLS service"]
}

while True:
    for i in commands:
        print(f"{i}. {commands[i][1]}")
    user_input = input("Please select a command:")
    if user_input == "KILL":
        break
    elif int(user_input) in commands:
        command = commands[int(user_input)][0]
        ip_address = input("Please enter the IP address: ") or "IP ADDRESS" #default IP
        print(f"\nCommand: {command} {ip_address}\n")
        os.system(f"{command} {ip_address}")
    else:
        print("Invalid input, please enter a number from the list above.")
    print("")

import os

commands = {
    1: ["-A 192.168.1.1", "Performs an aggressive scan on IP address '192.168.1.1'"],
    2: ["-O 192.168.1.1", "Tries to determine the operating system of host '192.168.1.1'"],
    3: ["-sS 192.168.1.1", "Performs a stealth SYN scan of host '192.168.1.1'"],
    4: ["-T1 192.168.1.1", "Performs a fast scan on IP address '192.168.1.1'"],
    5: ["-T4 192.168.1.1", "Performs an intense scan on IP address '192.168.1.1'"],
    6: ["-sP 192.168.1.1", "Performs a ping scan on IP address '192.168.1.1'"],
    7: ["-Pn 192.168.1.1", "Performs a scan without sending a ping request to IP address '192.168.1.1'"],
    8: ["-sA 192.168.1.1", "Performs an ACK scan on IP address '192.168.1.1'"],
    9: ["-SL 192.168.1.1", "Performs a scan for SSL/TLS service on IP address '192.168.1.1'"]
}

while True:
    for i in commands:
        print(f"{i}. {commands[i][1]}")
    user_input = input("Please select a command:")
    if user_input == "KILL":
        break
    elif int(user_input) in commands:
        command = commands[int(user_input)][0]
        print(f"\nCommand: {command}\n")
    else:
        print("Invalid input, please enter a number from the list above.")
    print("")

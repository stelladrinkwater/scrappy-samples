import argparse
import sys
from pythonosc.udp_client import SimpleUDPClient

# Define the default OSC server parameters
OSC_IP = "127.0.0.1"
OSC_PORT = 2390

# Create an OSC client
client = SimpleUDPClient(OSC_IP, OSC_PORT)

print(f"Sending OSC messages to {OSC_IP}:{OSC_PORT}. Type your message and press enter to send.")
print("Format: /address value1 value2 ...")

while True:
    try:
        user_input = input("OSC> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        
        parts = user_input.split()
        if len(parts) < 1:
            print("Invalid input. Must contain at least an OSC address.")
            continue
        
        address = parts[0]
        arguments = []
        
        for arg in parts[1:]:
            try:
                if '.' in arg:
                    arguments.append(float(arg))
                else:
                    arguments.append(int(arg))
            except ValueError:
                arguments.append(arg)
        
        client.send_message(address, arguments)
        print(f"Sent: {address} {arguments}")
    
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

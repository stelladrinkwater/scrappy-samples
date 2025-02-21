from pythonosc import dispatcher, osc_server
import asyncio
import sys
from time import sleep
from datafeel.device import VibrationMode, discover_devices, LedMode, ThermalMode

# Define the port to listen on
OSC_PORT = 2390

# Discover DataFeel devices
devices = discover_devices(4)
if not devices:
    print("No DataFeel devices found. Exiting...")
    sys.exit(1)

device = devices[0]
print(f"Connected to DataFeel device: {device}")

def handle_osc_message(address, *args):
    print(f"Received OSC Message: {address} {args}")
    if len(args) < 2:
        print("Invalid OSC message format.")
        return

    try:
        dot_index = int(args[0])
        command = str(args[1]).lower()
    except ValueError:
        print("Invalid dot index or command.")
        return

    if command == "vibration" and len(args) == 5:
        try:
            frequency = float(args[2])
            intensity = float(args[3])
            duration = int(args[4])
            print(f"Setting vibration on dot {dot_index}: freq={frequency}, intensity={intensity} for {duration}ms")
            device.registers.set_vibration_mode(VibrationMode.MANUAL)
            device.play_frequency(frequency, intensity)
            sleep(duration / 1000.0)
            device.stop_vibration()
        except ValueError:
            print("Invalid vibration parameters.")

    elif command == "light" and len(args) == 5:
        try:
            red = float(args[2])
            green = float(args[3])
            blue = float(args[4])
            print(f"Setting light on dot {dot_index}: R={red}, G={green}, B={blue}")
            device.set_led(int(red * 255), int(green * 255), int(blue * 255))
        except ValueError:
            print("Invalid light parameters.")

    elif command == "temperature" and len(args) == 3:
        try:
            temp = float(args[2])
            print(f"Setting temperature on dot {dot_index}: level={temp}")
            device.activate_thermal_intensity_control(temp)
        except ValueError:
            print("Invalid temperature parameter.")

    else:
        print("Unknown command or incorrect parameters.")

async def run_osc_server():
    disp = dispatcher.Dispatcher()
    disp.map("/*", handle_osc_message)
    server = osc_server.AsyncIOOSCUDPServer(("0.0.0.0", OSC_PORT), disp, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()
    print(f"Listening for OSC messages on port {OSC_PORT}...")
    
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(run_osc_server())

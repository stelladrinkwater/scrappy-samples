from time import sleep
from datafeel.device import VibrationMode, discover_devices, LedMode
import keyboard
import threading

# Discover available devices
devices = discover_devices(4)
if len(devices) < 4:
    print("Not enough devices found.")
    exit()

dot_keys = {
    devices[0]: "12345678",
    devices[1]: "qwertyui",
    devices[2]: "asdfghjk",
    devices[3]: "zxcvbnm,"
}

# Define a mapping of frequencies to RGB color values
note_map = {
    '1': (110, (255, 0, 0)), '2': (123, (255, 165, 0)), '3': (139, (255, 255, 0)),
    '4': (147, (0, 255, 0)), '5': (165, (0, 255, 255)), '6': (185, (0, 0, 255)),
    '7': (208, (128, 0, 128)), '8': (220, (255, 255, 255)),
    'q': (110, (255, 0, 0)), 'w': (123, (255, 165, 0)), 'e': (139, (255, 255, 0)),
    'r': (147, (0, 255, 0)), 't': (165, (0, 255, 255)), 'y': (185, (0, 0, 255)),
    'u': (208, (128, 0, 128)), 'i': (220, (255, 255, 255)),
    'a': (110, (255, 0, 0)), 's': (123, (255, 165, 0)), 'd': (139, (255, 255, 0)),
    'f': (147, (0, 255, 0)), 'g': (165, (0, 255, 255)), 'h': (185, (0, 0, 255)),
    'j': (208, (128, 0, 128)), 'k': (220, (255, 255, 255)),
    'z': (110, (255, 0, 0)), 'x': (123, (255, 165, 0)), 'c': (139, (255, 255, 0)),
    'v': (147, (0, 255, 0)), 'b': (165, (0, 255, 255)), 'n': (185, (0, 0, 255)),
    'm': (208, (128, 0, 128)), ',': (220, (255, 255, 255))
}

# Set up dots for manual vibration and LED control
for device in devices:
    device.registers.set_vibration_mode(VibrationMode.MANUAL)
    device.registers.set_led_mode(LedMode.GLOBAL_MANUAL)

print("Play notes using assigned keys.")

active_keys = set()
lock = threading.Lock()

def update_devices():
    while True:
        with lock:
            for device, keys in dot_keys.items():
                active_device_keys = [key for key in active_keys if key in keys]
                if active_device_keys:
                    key = active_device_keys[-1]  # Use the most recently pressed key
                    freq, color = note_map[key]
                    r, g, b = color
                    device.set_led(r, g, b)
                    device.play_frequency(freq, 1.0)
                else:
                    device.stop_vibration()
                    device.set_led(0, 0, 0)
        sleep(0.05)  # Improve responsiveness

def handle_key_event(event):
    with lock:
        if event.event_type == keyboard.KEY_DOWN and event.name in note_map:
            active_keys.add(event.name)
        elif event.event_type == keyboard.KEY_UP and event.name in note_map:
            active_keys.discard(event.name)

# Start a background thread to handle updates
threading.Thread(target=update_devices, daemon=True).start()
keyboard.hook(handle_key_event)
keyboard.wait()

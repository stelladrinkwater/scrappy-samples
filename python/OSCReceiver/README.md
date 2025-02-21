# DataFeel OSC Control Script

## Overview
This Python script sets up an OSC (Open Sound Control) server to control DataFeel haptic devices. It allows users to send OSC messages to control vibration, LED lighting, and thermal settings on connected DataFeel devices.

## Features
- **Vibration Control**: Set frequency, intensity, and duration for vibration feedback.
- **LED Control**: Adjust the red, green, and blue values to change the color of the LEDs.
- **Thermal Control**: Set the temperature level for haptic feedback.
- **OSC Communication**: The script listens on port `2390` for incoming OSC messages and parses them to apply commands to the DataFeel device.

## Prerequisites
### Software Requirements
- Python 3.x
- Required Python libraries:
  - `python-osc`
  - `asyncio`
  - `datafeel`

To install dependencies, run:
```sh
pip install python-osc asyncio datafeel
```

### Hardware Requirements
- DataFeel haptic devices connected via USB or Bluetooth

## Usage
1. Ensure the DataFeel device is powered on and connected.
2. Run the script:
   ```sh
   python script.py
   ```
3. Send OSC messages to the script using an OSC client (e.g., TouchOSC, Max/MSP, or Pure Data) with the following message formats:

### OSC Message Formats
#### Vibration Command:
```
/vibration [dot_index] [frequency] [intensity] [duration]
```
**Example:**
```
/vibration 0 200.0 1.0 500
```
This sets vibration on dot `0` to `200Hz` with `1.0` intensity for `500ms`.

#### LED Command:
```
/light [dot_index] [red] [green] [blue]
```
**Example:**
```
/light 0 1.0 0.0 0.5
```
This sets the LED color of dot `0` to a mix of red and blue.

#### Thermal Command:
```
/temperature [dot_index] [level]
```
**Example:**
```
/temperature 0 0.5
```
This sets the temperature level on dot `0` to `0.5` (arbitrary unit based on the API).

## Code Structure
- **Discover DataFeel Devices**: The script discovers and connects to available DataFeel devices.
- **OSC Server Setup**: The script sets up an asynchronous OSC server listening on port `2390`.
- **Message Parsing**: Incoming OSC messages are parsed and mapped to corresponding device actions.
- **Device Control**: Commands are executed to adjust vibration, LED, or thermal settings.

## Troubleshooting
- **No device detected**: Ensure the DataFeel device is powered on and properly connected.
- **OSC messages not triggering actions**: Verify that the OSC client is sending messages to the correct IP and port (`2390`).
- **Incorrect command parameters**: Check message format and ensure values are within valid ranges.

## Author
Daniel Lindenberger (daniel@bangingrocks.ca)

## License
MIT


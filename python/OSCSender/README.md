# DataFeel OSC Client Script

## Overview
This Python script provides an interactive command-line interface to send OSC (Open Sound Control) messages to an OSC server. It allows users to input custom OSC addresses and values, which are then transmitted to the specified OSC server.

## Features
- **Interactive Command-Line Interface**: Users can enter OSC messages dynamically.
- **OSC Message Transmission**: Sends messages to a designated OSC server.
- **Flexible Data Handling**: Supports integer, float, and string values.

## Prerequisites
### Software Requirements
- Python 3.x
- Required Python libraries:
  - `python-osc`

To install dependencies, run:
```sh
pip install python-osc
```

## Usage
1. Set the OSC server IP and port in the script by modifying these lines:
   ```python
   OSC_IP = "127.0.0.1"  # Change this to the target server IP
   OSC_PORT = 2390  # Change this to the desired port
   ```
2. Run the script:
   ```sh
   python script.py
   ```
3. Enter OSC messages in the following format:
   ```
   /address value1 value2 ...
   ```
4. Type `exit` or `quit` to terminate the script.

### Example OSC Messages
#### Single Value:
```
/test 42
```
Sends an OSC message to `/test` with the integer `42`.

#### Multiple Values:
```
/light 1 0.5 0.7 1.0
```
Sends an OSC message to `/light` with three floating-point values.

## Code Structure
- **Define OSC Server Parameters**: Sets the IP and port for OSC communication.
- **Create an OSC Client**: Establishes a UDP client to send messages.
- **User Input Handling**: Processes user-provided OSC messages and extracts arguments.
- **Send Messages**: Formats and transmits messages based on user input.

## Troubleshooting
- **No response from the server**: Ensure the target OSC server is running and listening on the specified IP and port (`127.0.0.1:2390`).
- **Incorrect message format**: Ensure messages start with a `/` followed by valid arguments.

## Author
Daniel Lindenberger (daniel@bangingrocks.ca)

## License
MIT


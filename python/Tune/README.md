# DataFeel Keyboard-Controlled Haptic Feedback Script

## Overview
This Python script allows users to play notes using a computer keyboard while controlling DataFeel haptic Dots. Each key is mapped to a vibration frequency and an LED color, enabling a tactile and visual representation of musical notes.

## Features
- **Keyboard-Based Control**: Each key corresponds to a specific frequency and LED color.
- **Multi-Dot Support**: Supports up to four DataFeel Dots.
- **Simultaneous Input**: Multiple keys can be pressed and processed in real-time.
- **Threaded Execution**: Ensures smooth updates to the haptic Dots without blocking input.

## Prerequisites
### Software Requirements
- Python 3.x
- Required Python libraries:
  - `datafeel`
  - `keyboard`
  - `threading`

To install dependencies, run:
```sh
pip install datafeel keyboard
```

### Hardware Requirements
- Up to four DataFeel Dots connected via USB.

## Usage
1. Ensure all DataFeel Dots are powered on and connected via USB.
2. Run the script:
   ```sh
   python script.py
   ```
3. Play notes using the assigned keys on your keyboard.
4. Press `Ctrl + C` or close the terminal to stop the script.

### Key Mappings
Each key is mapped to a vibration frequency (Hz) and an LED color (RGB). Some example mappings:
```
'1' -> 110 Hz, Red (255, 0, 0)
'2' -> 123 Hz, Orange (255, 165, 0)
'3' -> 139 Hz, Yellow (255, 255, 0)
'4' -> 147 Hz, Green (0, 255, 0)
'5' -> 165 Hz, Cyan (0, 255, 255)
'6' -> 185 Hz, Blue (0, 0, 255)
'7' -> 208 Hz, Purple (128, 0, 128)
'8' -> 220 Hz, White (255, 255, 255)

'q-i', 'a-k', and 'z-,' keys are also mapped to the same frequencies and colors as '1-8'.
```

## Code Structure
- **Dot Discovery**: Finds and connects to available DataFeel Dots.
- **Threaded Background Processing**: Continuously updates the active Dots with vibration and LED settings.
- **Keyboard Event Handling**: Detects key presses and maps them to corresponding actions.
- **Real-Time Feedback**: Ensures an interactive experience by immediately reflecting key presses in haptic feedback.

## Troubleshooting
- **Not enough Dots found**: Ensure up to four DataFeel Dots are connected via USB.
- **No vibration or LED response**: Verify the Dots are properly connected and powered on.
- **Keys not responding**: Ensure no other application is intercepting keyboard events.

## Author
Daniel Lindenberger (daniel@bangingrocks.ca)

## License
MIT


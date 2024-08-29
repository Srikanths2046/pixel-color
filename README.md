# Pixel color

A simple Python program that provides the RGB hex values of the color under the mouse cursor in real time. This tool captures the screen and determines the color of the pixel directly under the cursor, displaying the color as a hexadecimal value.

### Features:
Displays the RGB hex value of the color under the cursor.
Updates the displayed color and hex value in real-time as the cursor moves.
Lightweight and easy to use with a simple GUI built using Tkinter.

### Easy to use:
![pixel-color-demo](https://github.com/user-attachments/assets/27011470-bcc4-4e90-b7c1-7813f3d7b1b8)

### Prerequisites:
Before you begin, ensure you have met the following requirements:
1. Python 3.12.5 installed on your machine.
2. pyautogui library: This library allows the program to capture the screen and retrieve the color under the cursor.
3. Pillow library: Used for pixel manipulation and retrieving color values.

### Installation:
To install the necessary libraries, you can use `pip`:

`pip install pyautogui Pillow`

### Usage:
1. Clone the Repository:<br>
`git clone https://github.com/Srikanths2046/pixel-color.git`<br>
`cd pixel-color/color-detector`<br>

2. Run the script using Python:<br>
`python color-detector.py`<br>

The program will display a small, floating window showing the color under the cursor and its corresponding hex value.

### How It Works:
1. The program captures the current position of the mouse cursor using pyautogui.
2. It takes a screenshot of the current screen and gets the RGB value of the pixel at the cursor position.
3. The RGB value is then converted to a hexadecimal string and displayed in the Tkinter window.
4. The window follows the cursor while remaining slightly offset to avoid covering it.

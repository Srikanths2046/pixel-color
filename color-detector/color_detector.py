import pyautogui
import colorsys
from tkinter import Tk, Label, Frame

def get_color_at_cursor():
    x, y = pyautogui.position()
    screenshot = pyautogui.screenshot()
    color = screenshot.getpixel((x, y))
    return color

def rgb_to_hex(rgb):
    # Convert RGB tuple to hexadecimal format
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def update_color_display():
    rgb_color = get_color_at_cursor()
    hex_color = rgb_to_hex(rgb_color)
    color_label.config(text=f"Hex: {hex_color}")
    color_indicator.config(bg=hex_color)
    move_window()
    root.after(100, update_color_display)

def move_window():
    # Get the current position of the mouse cursor
    x, y = pyautogui.position()
    # Offset the window position slightly so it doesn't cover the cursor
    root.geometry(f'+{x + 20}+{y + 20}')

# Create the main window
root = Tk()
root.overrideredirect(True)  # Removes the window decorations (title bar, etc.)
root.attributes('-topmost', True)  # Keeps the window on top

# Create a frame to contain the color indicator and label
frame = Frame(root, bd=1, relief='solid')
frame.pack()

# Add a color indicator (small square that shows the current color)
color_indicator = Frame(frame, width=50, height=50, bg='#000000', bd=1, relief='solid')
color_indicator.grid(row=0, column=0, padx=5, pady=5)

# Add a label to display the hex color value
color_label = Label(frame, text="Hex: #000000", font=('Helvetica', 12))
color_label.grid(row=0, column=1, padx=5)

# Start the color update loop
update_color_display()

root.mainloop()

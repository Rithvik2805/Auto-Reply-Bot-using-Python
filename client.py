import pyautogui
import time

def show_mouse_position():
    print("Press Ctrl+C to stop...\n")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse position: ({x}, {y})", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped tracking mouse position.")

if __name__ == "__main__":
    show_mouse_position()

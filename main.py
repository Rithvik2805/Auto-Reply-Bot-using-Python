import os
import pyautogui
import pyperclip
import time
from openai import OpenAI

# Set your key using environment variable instead of hardcoding
# Example in terminal: setx OPENAI_API_KEY "your_api_key"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# HELPER FUNCTIONS
def get_chat_history(region_coords):
    try:
        start_x, start_y, end_x, end_y = region_coords
        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragTo(end_x, end_y, duration=1.0, button='left')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        return pyperclip.paste().strip()
    except Exception as e:
        print(f"[ERROR] Failed to copy chat: {e}")
        return ""

def send_message(response, message_box_coords):
    try:
        x, y = message_box_coords
        pyautogui.click(x, y)
        pyperclip.copy(response)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    except Exception as e:
        print(f"[ERROR] Failed to send message: {e}")

def generate_ai_response(chat_history):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are (your name) from India, bilingual (English and Telugu). "
                        "Respond naturally as if chatting in a friendly conversation."
                    )
                },
                {"role": "user", "content": chat_history}
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] OpenAI API call failed: {e}")
        return "Sorry, something went wrong while generating my response."

# MAIN CHAT AUTOMATION LOOP
def main():
    print("Starting chat automation... Press Ctrl+C to stop anytime.")

    # Step 1: Click on the chat icon (adjust these coordinates)
    chat_icon_coords = (1410, 1169)
    text_region = (706, 278, 1791, 1084)
    message_box_coords = (905, 1091)

    pyautogui.click(*chat_icon_coords)
    time.sleep(1)

    while True:
        chat_history = get_chat_history(text_region)

        if not chat_history:
            print("No text found, retrying...")
            time.sleep(3)
            continue

        print("\n[DEBUG] Chat history captured.")
        print(chat_history[:300], "...\n")  # preview first 300 chars

        ai_reply = generate_ai_response(chat_history)
        print(f"[AI Reply] {ai_reply}\n")

        send_message(ai_reply, message_box_coords)

        print("[INFO] Message sent. Waiting for new messages...\n")
        time.sleep(10)  # avoid spamming or overloading API

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAutomation stopped by user.")

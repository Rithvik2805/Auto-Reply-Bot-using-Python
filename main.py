import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key="enter the api key",
    )

def is_last_message_from_sender(chat_log, sender_name="name"):
    #split the chat log into individual messages
    messages = chat_log.strip().split("/2025]")[-1]
    if sender_name in messages:
        return True
    return False

# Step 1: Click on the icon at (1274,1165)
pyautogui.click(1274,1165)
time.sleep(1) #wait for 1 second to ensure that the click is registered
while True:
    
    # Step 2: Move the mouse to the starting point of the text selection (767,278) to (1748,1020)
    pyautogui.moveTo(764,355)
    pyautogui.dragTo(1763,1016,duration=1.0,button='left') # drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(773,1074)
    time.sleep(1) #wait for 1 second to ensure that the copy command is completed


    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the selected text to verify
    print(chat_history)

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a person named (your name) who speaks english as well as telugu You are from india. You analyze chat history and respond like (your name) . Output should be the next chat response (text message only)"
          },
        {"role": "user", "content":chat_history}
      ]
    )
      
    response = completion.choices[0].message.content
    pyperclip.copy(response)

    # Step 6: Click at (937,1074)
    pyautogui.click(946,1082)
    time.sleep(1)

    # Step 7: Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # Step 8: Press Enter
    pyautogui.press('enter')

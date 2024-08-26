from Mistral import get_ai_response
from Screenshot import take_screenshot
from Dialogue import Dialogue
from ScreenshotReader import screenshot_to_string
import keyboard as Keyboard
import threading as Threads
import time as Time
from DiscordBot import *
import asyncio

# ctrl+shift+p to open up venv
# https://docs.mistral.ai/getting-started/quickstart/
# Tesseract installer https://github.com/UB-Mannheim/tesseract/wiki
# TOP_LEFT: 865, 575
# BOTTOM_LEFT: 865, 803
# TOP_RIGHT: 1591, 575
# BOTTOM_RIGHT: 1591, 803

CONSTANTS = {
    "TOP": 575,
    "RIGHT": 1591,
    "BOTTOM": 758,
    "LEFT": 899,
    "TESSERACT_PATH": "C:\\Program Files\\Tesseract-OCR\\tesseract.exe",
    "IMAGE_NAME": "screenshot.png",
    "SCREENSHOT_HOTKEY": "ctrl + shift + a",
    "WINDOW_TITLE": "King of the Castle",
    "ESCAPE_HOTKEY": "esc",
    "DISCORD_TOKEN": "MTI3NzQ0NTUyMzgyMDc3NzUxMw.G0nB20.RZ_ORQYTzMx4SGqnyF3grfX4J5wSGJxTeXGJzY",
    "CHANNEL": 709408355181002847
}

def global_hotkeys():
    print("Thread 1 running")
    Keyboard.add_hotkey(CONSTANTS["SCREENSHOT_HOTKEY"], magic)
    Keyboard.wait(CONSTANTS["ESCAPE_HOTKEY"]) 

def boxes():
    Dialogue("Test Dialogue", "HELLO")
    
def screenshot_to_ai(file_name: str) -> None:
    input = screenshot_to_string(CONSTANTS["TESSERACT_PATH"], file_name)
    prefix = "Convert the following into something Lin Manuel Miranda would write in Hamilton in one stanza: "
    response = get_ai_response(prefix + input)
    print(response)
    Dialogue("Mistral Response", response)

def full_dialogue_listener():
    prev_len = 0
    while True: 

        take_screenshot(
        CONSTANTS["WINDOW_TITLE"],
        CONSTANTS["LEFT"],
        CONSTANTS["TOP"],
        CONSTANTS["RIGHT"],
        CONSTANTS["BOTTOM"],
        "current.png")
        current_content = screenshot_to_string(CONSTANTS["TESSERACT_PATH"], "current.png")
        
        Time.sleep(0.5)

        take_screenshot(
        CONSTANTS["WINDOW_TITLE"],
        CONSTANTS["LEFT"],
        CONSTANTS["TOP"],
        CONSTANTS["RIGHT"],
        CONSTANTS["BOTTOM"],
        "next.png")
        next_content = screenshot_to_string(CONSTANTS["TESSERACT_PATH"], "next.png")

        if isValidDialogue(current_content, next_content, prev_len):
            print("\n" + current_content + "\nlen: " + str(len(current_content)) + "\n")
            prev_len = len(current_content)
            screenshot_to_ai(current_content)
            
def magic():
    take_screenshot(
        CONSTANTS["LEFT"],
        CONSTANTS["TOP"],
        CONSTANTS["RIGHT"],
        CONSTANTS["BOTTOM"],
        "screenshot.png")
    screenshot_to_ai("screenshot.png")
    asyncio(send_msg(CONSTANTS["CHANNEL"], "HELLO"))

def isValidDialogue(current_content, next_content, prev_len) -> bool:
    curr_len = len(current_content)
    next_len = len(next_content)
    if curr_len == 0:
        return False
    elif curr_len < 90:
        return False
    elif curr_len != next_len:
        return False
    elif curr_len == prev_len:
        print("len: " + str(curr_len))
        return False
    return True
    

def discord():
    print("Thread 3 running")
    run_bot()
    asyncio.run(send_msg(CONSTANTS["CHANNEL"], "THIS IS THREAD 2"))

if __name__ == "__main__":

    thread1 = Threads.Thread(target=global_hotkeys)
    thread1.start()
    thread3 = Threads.Thread(target=discord)
    thread3.start()


    thread1.join()
    thread3.join()
    
    
        
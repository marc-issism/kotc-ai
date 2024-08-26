import ctypes

def Dialogue(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)
 
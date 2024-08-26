from PIL import ImageGrab
from Windows import move_window, maximize_window, focus_window
from Dialogue import Dialogue

def take_screenshot(left: int, top: int, right: int, bottom: int, file_name: str) -> None:
    """Takes a screenshot of a window given by its title. The screenshot taken is contained within the coordinates
        'left', 'top', 'right', and 'bottom'. It also brings that window into focus.
    """
    try:
        #move_window(window_title, 0, 0)
        #maximize_window(window_title)
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        screenshot.save(file_name)
        screenshot.close()
    except:
        Dialogue("Error", "Window not found")

    

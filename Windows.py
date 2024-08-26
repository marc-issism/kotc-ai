import pygetwindow as GetWindow

def focus_window(window_title: str) -> None:
    window = GetWindow.getWindowsWithTitle(window_title)[0]
    window.activate()

def maximize_window(window_title: str) -> None:
    window = GetWindow.getWindowsWithTitle(window_title)[0]
    window.maximize()

def move_window(window_title: str, x_coordinate: int, y_coordinate: int) -> None:
    window = GetWindow.getWindowsWithTitle(window_title)[0]
    window.moveTo(x_coordinate, y_coordinate)
    window.maximize()
    window.activate()
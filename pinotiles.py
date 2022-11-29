import pyautogui
import win32api as win
import win32con as con
while True:
    for i in [480,630,780,910]:
        pixel=pyautogui.pixel(i,450)
        if pixel[0]<20:
            win.SetCursorpos((i,500))
            win.mouse_event(
                con.MOUSEEVENTF_LEFTDOWN,0,0
            )
            win.mouse_event(
                con.MOUSEEVENTF_LEFTUP,0,0
            )
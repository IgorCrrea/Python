import time
from platform import system

import webbrowser as web
import pyautogui as pg



def sendwhats_image(phone_no: str, img_path: str, caption: str = " ", wait_time: int = 15,
                    tab_close: bool = False, close_time: int = 3) -> None:
    """Send Image to a WhatsApp Contact"""

    web.open('https://web.whatsapp.com/send?phone=' +
             phone_no + '&text=' + caption)
    time.sleep(10)
    width, height = pg.size()
    pg.click(width / 1.04, height / 2)
    time.sleep(wait_time - 2)

    if system().lower() == "windows":
        import win32clipboard
        from io import BytesIO

        from PIL import Image
        
        image = Image.open(img_path)
        output = BytesIO()
        image.convert('RGB').save(output, "BMP")
        data = output.getvalue()[14:]
        time.sleep(5)
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        time.sleep(5)
        pg.hotkey("ctrl", "v")
    else:
        print(f"{system().lower()} not supported!")
        return
    time.sleep(wait_time)
    pg.press('enter')
    if tab_close:
        close_tab(wait_time=close_time)
        
def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        pg.hotkey("ctrl", "w")
    elif system().lower() in "darwin":
        pg.hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")
    pg.press("enter")
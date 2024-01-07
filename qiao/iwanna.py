import cv2
import pyautogui
import utils

from importlib import resources
from PIL import Image

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1


press_m_key = utils.load_image("data/press_m_key.jpg")
screenshot = utils.screenshot()

locs = utils.sub_image(screenshot, press_m_key, confidence=0.9)
if locs.size > 0:
    y, x = locs[0]
    # height, width = press_m_key.shape[0:2]
    # img = cv2.rectangle(screenshot, (x, y), (x + width, y + height), (0, 0, 255), 2)
    # cv2.imshow("screenshot", img)
    pyautogui.leftClick(x, y)
    pyautogui.press("m")

cv2.waitKey(0)

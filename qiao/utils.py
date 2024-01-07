import os
import cv2
import numpy as np
import pyautogui

from importlib import resources
from PIL import Image


def load_image(resource_name: str):
    if __package__:
        d = resources.files(__package__)
        with resources.as_file(d.joinpath(resource_name)) as path:
            return cv2.imread(path)
    else:
        d = os.path.dirname(__file__)
        path = os.path.join(d, resource_name)
        return cv2.imread(path)

def pil2cv2(img: Image, grayscale=False):
    img_array = np.array(img.convert('RGB'))
    img_cv = img_array[:, :, ::-1].copy()  # -1 does RGB -> BGR
    if grayscale:
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    return img_cv

def screenshot():
    return pil2cv2(pyautogui.screenshot())

def sub_image(img, sub, confidence=0.99):
    # get all matches at once, credit: https://stackoverflow.com/questions/7670112/finding-a-subimage-inside-a-numpy-image/9253805#9253805
    result = cv2.matchTemplate(img, sub, cv2.TM_CCOEFF_NORMED)
    return np.argwhere(result >= confidence)

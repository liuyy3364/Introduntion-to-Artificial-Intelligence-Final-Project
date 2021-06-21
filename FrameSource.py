# 301 OK
class FrameSource_Template:
    def __init__(self)->None:
        pass

    def get_frame(self):
        pass

import cv2
class TownCentre:
    def __init__(self)->None:
        self.cap = cv2.VideoCapture("resources/TownCentreXVID.mp4")
    def get_frame(self):
        return self.cap.read()[1]

# 301 OK
class FrameSource_Template:
    def __init__(self)->None:
        """
        function的說明
        """
        raise Exception("using template class")

    def get_frame(self):
        """
        return: one frame read from the source
        """
        raise Exception("not implemented")

import cv2
class TownCentre:
    def __init__(self)->None:
        self.cap = cv2.VideoCapture("resources/TownCentreXVID.mp4")
    def get_frame(self):
        return self.cap.read()[1]

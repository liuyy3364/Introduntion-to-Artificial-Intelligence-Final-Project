#310
import webserver
from threading import Thread
import cv2
class Displayer_Template:
    def __init__(self) -> None:
        """
        function的說明
        """
        raise Exception("using template class")

    def update_frame(self, frame):
        """
        update currently displaying frame
        """
        raise Exception("not implemented")

    def run(self):
        """
        start displaying frames
        """
        raise Exception("not implemented")

import imutils
class Flask_VidStream:
    frame = bytes()

    def update_frame(self, frame):
        self.frame = frame
        frame = imutils.resize(self.frame,height=720)
        ret , jpg = cv2.imencode(".jpg", frame)
        jpg = jpg.tobytes()
        webserver.frame_wrapper[0] = jpg
    
    def run(self):
        """
        function的說明
        開一個thread跑web_server
        """
        t = Thread(target=webserver.web_server, args=())
        t.daemon = True
        t.start()


#310
import webserver
from threading import Thread
import cv2
class Displayer_Template:
    #麻煩 class 名稱第一個字母大寫
    def __init__(self) -> None:
        """
        function的說明
        """
        raise Exception("use empty class")

    def update_frame(self, frame):
        """
        function的說明
        """
        raise Exception("not implemented")

    def run(self):
        """
        function的說明
        """
        raise Exception("not implemented")

class Flask_VidStream:
    #麻煩 class 名稱第一個字母大寫
    frame = bytes()

    def update_frame(self, frame):
        self.frame = frame
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


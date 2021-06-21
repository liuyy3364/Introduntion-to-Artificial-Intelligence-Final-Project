#059 base
import numpy as np

class Detector:
    #麻煩 class 名稱第一個字母大寫
    class Haar:
        def __init__(self) -> None:
            """
            Load the cascade
            """
            # raise Exception("use empty class")
            self.model = cv2.CascadeClassifier('reference/haarcascade_fullbody.xml')
        
        def detect(self, frame: np.ndarray) -> list:
            """
            frame: a frame
            ret: a list of bounded box[x, y, w, h]
            """
            # raise Exception("not implemented")
            # Load the cascade
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            persons = self.model.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
            return persons


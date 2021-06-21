#059 base OK
import numpy as np
import cv2

class Detector_Template:
    #麻煩 class 名稱第一個字母大寫
    def __init__(self) -> None:
        """
        function的說明
        """
        raise Exception("use empty class")

    def detect(self, frame: np.ndarray) -> list:
        """
        function的說明
        """
        raise Exception("not implemented")


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

class YOLOv5:
    #麻煩 class 名稱第一個字母大寫
    def __init__(self, interest_label="person") -> None:
        """
        yolov5 detector
        """
        # Model
        self.interest_label = interest_label
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def detect(self, frame: np.ndarray) -> list:
        """
        return bounding boxe [(x,y,w,h)...]
        """
        result = self.model(frame).pandas().xyxy[0]
        # format xywh
        boxes=[]
        for i, n in enumerate(result['name']):
            if n==self.interest_label:
                x = int(result['xmin'][i]) 
                y = int(result['ymin'][i]) 
                w = int(result['xmax'][i]) - x
                h = int(result['ymax'][i]) - y
                boxes.append((x,y,w,h))

        return boxes

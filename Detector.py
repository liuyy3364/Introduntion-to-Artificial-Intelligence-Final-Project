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
        ret: a list of bounded box[x, y, x, y]
        """
        # raise Exception("not implemented")
        # Load the cascade
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        persons = self.model.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
        scores = [1]*len(persons)
        for i, (x, y, w, h) in enumerate(persons):
            persons[i] = (x,y,x+w,y+h)
        return persons, scores


import torch
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
        return bounding boxe [(x,y,x,y)...]
        """
        result = self.model(frame).pandas().xyxy[0]
        # format xywh
        boxes = []
        scores = []
        for i, n in enumerate(result['name']):
            if n==self.interest_label:
                if result['confidence'][i] < 0.35:
                    continue
                xmin = int(result['xmin'][i]) 
                ymin = int(result['ymin'][i]) 
                xmax = int(result['xmax'][i])
                ymax = int(result['ymax'][i])
                boxes.append((xmin, ymin, xmax, ymax))
                scores.append(result['confidence'][i])

        return boxes, scores

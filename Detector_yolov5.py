import cv2
import torch
from PIL import Image

#059 base
import numpy as np

class yolov5:
    #麻煩 class 名稱第一個字母大寫
    def __init__(self) -> None:
        """
        function的說明
        """
        # Model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def detect(self, frame: np.ndarray) -> list:
        """
        function的說明
        """
        result = self.model(frame).pandas().xyxy[0]




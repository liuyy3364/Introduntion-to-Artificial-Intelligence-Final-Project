# 301  OK
import Detector
import Tracker 
import Displayer
import Benchmarker
import Optimizer
import FrameSource
import cv2
import numpy as np
import time
from typing import Tuple, List

class Framework():
    t0=0
    t1=0
    fps=0
    def __init__(self, frame_source='Camera', detector='Haar', interest_label="person",
                tracker='Tracker', displayer='Displayer', 
                benchmarker='Benchmarker', optimizer='Optimizer') -> None:      
        """
        function的說明
        """
        frame_source = getattr(FrameSource, frame_source)
        self.frame_source = frame_source()
        # self.frame_source = FrameSource.Camera()

        detector = getattr(Detector, detector)
        if detector=='yolov5':
            self.detector = detector(interest_label=interest_label)
        else:
            self.detector = detector()
        # self.detector = Detector.Detector()

        tracker = getattr(Tracker, tracker)
        self.tracker = tracker()
        # self.tracker = Tracker.Tracker()

        displayer = getattr(Displayer, displayer)
        self.displayer = displayer()
        # self.displayer = Displayer.Displayer()

        benchmarker = getattr(Benchmarker, benchmarker)
        self.benchmarker = benchmarker()
        # self.benchmarker = Benchmarker.Benchmarker()

        optimizer = getattr(Optimizer, optimizer)
        self.optimizer = optimizer()
        # self.optimizer = Optimizer.Optimizer()

    def detect(self, frame) -> List[Tuple[int,int,int,int]]:
        """
        frame: input frame
        return: a list of bounding boxes
        """
        return self.detector.detect(frame)
    
    def track(self, bounding_boxes) -> List[str]:
        """
        input: a list of bounding boxes
        return: a list of IDs
        """
        return self.tracker.track(bounding_boxes)
    
    def benchmark(self) -> list:
        return self.benchmarker.run()
    
    def optimize(self) -> list:
        return self.optimizer.optimize()

    def run_1_frame(self,draw=False) -> Tuple[List[Tuple[int,int,int,int]], List[str], float]:
        """
        return: 
            bounding_boxes: list(TBD)
            IDs: list(str)
            fps: float
        """
        self.t1 = time.time()
        self.fps = 1 / (self.t1 - self.t0)
        self.t0 = time.time()
        frame = self.frame_source.get_frame()
        bounding_boxes = self.detect(frame)
        IDs = self.track(bounding_boxes)
        if draw:
            cv2.rectangle(frame, (0, 0), (45, 12), (0, 0, 255), -1)
            cv2.putText(frame, "FPS "+str(self.fps), (1, 10), cv2.FONT_HERSHEY_TRIPLEX, 0.35, (0,0,0))
            for (x, y, w, h), id in zip(bounding_boxes, IDs):
                    # draw bounding box
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
                    # put id
                    cv2.rectangle(frame, (x, y-12), (x+21, y), (0, 0, 255), -1)
                    cv2.putText(frame, str(id), (x, y-2), cv2.FONT_HERSHEY_TRIPLEX, 0.35, (0,0,0))
        return frame, bounding_boxes, IDs, self.fps

    def run_and_display(self):
        self.displayer.run()
        while 1:
            frame, boxes, IDs, fps = self.run_1_frame()
            cv2.rectangle(frame, (0, 0), (50, 20), (0, 0, 255), -1)
            cv2.putText(frame, str(fps), (5, 15), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0))
            for (x, y, w, h), id in zip(boxes, IDs):
                    # draw bounding box
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
                    # put id
                    cv2.rectangle(frame, (x, y-12), (x+21, y), (0, 0, 255), -1)
                    cv2.putText(frame, str(id), (x, y-2), cv2.FONT_HERSHEY_TRIPLEX, 0.35, (0,0,0))
            self.displayer.update_frame(frame)
        

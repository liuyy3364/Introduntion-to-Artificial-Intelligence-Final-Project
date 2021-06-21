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
    def __init__(self, frame_source='TownCentre', detector='YOLOv5', interest_label="person",
                tracker='SORT', displayer='Flask_VidStream', 
                optimizer='Netadapt') -> None:      
        """
        function的說明
        """
        frame_source = getattr(FrameSource, frame_source)
        self.frame_source = frame_source()
        # self.frame_source = FrameSource.Camera()

        detector = getattr(Detector, detector)
        if detector=='YOLOv5':
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

        optimizer = getattr(Optimizer, optimizer)
        self.optimizer = optimizer()
        # self.optimizer = Optimizer.Optimizer()

    def detect(self, frame) -> List[Tuple[int,int,int,int]]:
        """
        frame: input frame
        return: a list of bounding boxes, confidence value
        """
        return self.detector.detect(frame)
    
    def track(self, bounding_boxes, scores) -> List[str]:
        """
        input: a list of bounding boxes (x, y, w, h, id)
        return: a list of boundings boxes with its id (x, y, x, y, id)
        """
        return self.tracker.track(bounding_boxes, scores)
    
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
        self.fps = round(1 / (self.t1 - self.t0),1)
        self.t0 = time.time()
        frame = self.frame_source.get_frame()
        bounding_boxes, score = self.detect(frame)
        BB_IDs = self.track(bounding_boxes, score)
        BB_IDs = BB_IDs.astype(np.int32)
        if draw:
            cv2.rectangle(frame, (0, 0), (150, 25), (0, 0, 255), -1)
            cv2.putText(frame, "FPS "+str(self.fps), (0, 25), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
            for xmin, ymin, xmax, ymax, id in BB_IDs:
                    # draw bounding box
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
                    # put id
                    cv2.rectangle(frame, (xmin,ymin-25), (xmin+50, ymin), (0, 0, 255), -1)
                    cv2.putText(frame, str(id), (xmin, ymin-2), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
        return frame, BB_IDs, self.fps

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
        

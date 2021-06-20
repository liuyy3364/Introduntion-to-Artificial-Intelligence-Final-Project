# 301
import Detector
import Tracker 
import Displayer
import Benchmarker
import Optimizer

class Framework():
    def __init__(self, detector='Detector', 
                tracker='Tracker', displayer='Displayer', 
                benchmarker='Benchmarker', optimizer='Optimizer') -> None:      
        """
        function的說明
        """
        detector = getattr(Detector, detector)
        self.detector = detector()

        tracker = getattr(Tracker, tracker)
        self.detector = tracker()

        displayer = getattr(Displayer, displayer)
        self.detector = displayer()

        benchmarker = getattr(Benchmarker, benchmarker)
        self.detector = benchmarker()

        optimizer = getattr(Optimizer, optimizer)
        self.detector = optimizer()

    # a list of bounding boxes
    def detect(self) -> list:
        """
        function的說明
        """
        return self.detector.detect()
    
    def

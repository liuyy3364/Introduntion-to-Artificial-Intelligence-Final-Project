#059 base
import numpy as np
from sort.sort import *

class Tracker_Template:
    def __init__(self) -> None:
        """
        function的說明
        """
        raise Exception("using template class")

    def track(self, bounding_boxes: list, scores: list) -> list:
        """
        do tracking according to detection results
        return: a list of boundings boxes with its id (x, y, w, h, id)
        """
        raise Exception("not implemented")

# SORT
class SORT:
    def __init__(self) -> None:
        """
        #create instance of SORT
        """
        # raise Exception("use empty class")
        self.mot_tracker = Sort(max_age=15, min_hits=1, iou_threshold=0.15)
    
    def track(self, track_bbs: list, scores: list) -> list:
        """
        track_bbs: a list of bounded boxes(x, y, w, h)
        ret: a list of boundings boxes with its id (x, y, w, h, id)
        """
        # raise Exception("not implemented")
        if len(track_bbs) == 0:
            persons = np.empty((0, 5))
        else:
            persons = np.concatenate((track_bbs,np.reshape(scores,(len(scores),1))),axis=1)
        track_bbs_ids = self.mot_tracker.update(persons)
        
        return track_bbs_ids
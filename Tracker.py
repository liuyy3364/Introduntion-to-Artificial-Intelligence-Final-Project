#059 base
import numpy as np
from sort.sort import *

class Tracker_Template:
    #麻煩 class 名稱第一個字母大寫
    def __init__(self) -> None:
        """
        function的說明
        """
        raise Exception("use empty class")

    def track(self) -> list:
        """
        function的說明
        """
        raise Exception("not implemented")

# SORT
import copy
def xywh_to_xyxy(bboxes: np.ndarray):
    ret = copy.deepcopy(bboxes)
    for i, (x, y, w, h) in enumerate(ret):
        ret[i] = (x, y, x+w, y+h)
    return ret

class SORT:
    def __init__(self) -> None:
        """
        #create instance of SORT
        """
        # raise Exception("use empty class")
        self.model = Sort(max_age=3, min_hits=1, iou_threshold=0.15)
    
    def track(self, track_bbs: np.ndarray) -> list:
        """
        track_bbs: a list of bounded boxes(x, y, w, h)
        ret: a list of ids
        """
        # raise Exception("not implemented")
        persons = xywh_to_xyxy(track_bbs)
        track_bbs_ids = mot_tracker.update(persons)
        ids = []
        for (x, y, w, h, bid) in track_bbs_ids:
            ids.append(bid)
        return ids
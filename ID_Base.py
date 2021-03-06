from collections import defaultdict

class ID_info:
    def __init__(self, id, x ,y ,last_frame):
        self.id = id
        self.pos0 = (x,y)
        self.pos1 = (x,y)
        self.last_frame = last_frame


class ID_Base():
    base = dict()
    def updateID(self, BB_IDs, frame_cnt):
        for i, (xmin, ymin, xmax, ymax, id) in enumerate(BB_IDs):
            if id in self.base.keys():
                self.base[id].pos1 = (xmin, ymin)
                self.base[id].last_frame = frame_cnt
            else:
                self.base[id] = ID_info(id, xmin, ymin, frame_cnt)
    
    def deleteID(self, id):
        del self.base[id]




# class ID_Base():
#     id_list = []
#     id_first = defaultdict(list)
#     id_last = defaultdict(list)
#     id_last_frame = defaultdict(int)

#     def updateID(self, bounding_boxes, IDs, frame_cnt):
#         for num, id in enumerate(IDs):
#             if id in self.id_list:
#                 self.id_last[str(id)] = bounding_boxes[num]
#                 self.id_last_frame[str(id)] = frame_cnt
#             else:
#                 self.id_list.append(id)
#                 self.id_first[str(id)]= bounding_boxes[num]
#                 self.id_last[str(id)] = bounding_boxes[num]
#                 self.id_last_frame[str(id)] = frame_cnt
    
    ############## debug code #################
        # print(self.id_first)
        # print(self.id_last)
        # print(self.id_last_frame)
    ###########################################       

    # def deleteID(self, id):
    #     del self.id_first[str(id)]
    #     del self.id_last[str(id)]
    #     del self.id_last_frame[str(id)]


############## debug code #################

# iid = ID_Base()
# cnt = 0
# while 1:
#     cnt += 1
#     tup = []
#     iids = []
#     inp = input("bounding_boxes, IDs")

#     if inp == "del":
#         inpu = input("what?\n")
#         iid.deleteID(str(inpu))
#     else:
#         inp = inp.split(",")
#         ids = inp[1]
#         inp = inp[0].split(";")
#         for i in range(len(inp)):
#             tuples = inp[i].split()
#             tup.append((int(tuples[0]), int(tuples[1]), int(tuples[2]), int(tuples[3])))
#         ids = ids.split()
#         for i in range(len(ids)):
#             iids.append(ids[i])
#         print(tup, iids, cnt)
#         iid.updateID(tup, iids, cnt)

    



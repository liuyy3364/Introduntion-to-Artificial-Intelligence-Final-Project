import framework
import ID_Base
import numpy as np

# Solving following system of linear equation
# ax + b = y
# ex.(-2, 14), (4, -4)
# -2a + 1b = 14
# 4a + 1b = -4
# a = np.array([[-2, 1],[4,1]])
# b = np.array([14, -4])
# a, b = np.linalg.solve(a,b) // a=-3, b=8 -
# y = -3x + 8                              |
# but frame's y is reverse                 |
# so y = 3x - 8 // a = - a, b = - b <-------

in_line = [(),()]
out_line = [(),()]

def equation(line):
    a = int(line[0][0])
    b = int(line[0][1])
    c = int(line[1][0])
    d = int(line[1][1])

    n = np.array([[a, 1], [c,1]])
    m = np.array([b, d])
    a, b = np.linalg.solve(n, m)
    return -a, -b

def check(first, last, in_line, out_line):
    p1 = (first[0], first[1])
    p2 = (last[0], last[1])
    a1, b1 = equation(in_line)
    a2, b2 = equation(out_line)
    
    if (a2 * p1[0] + b2 - p1[1]) >= 0: # first appear not in out_area
        if (a2 * p2[0] + b2 - p2[1]) <= 0: # last appear in out_area
            return 1
    elif (a1 * p1[0] + b1 - p1[1]) <= 0: # first appear not in in_area
        if (a1 * p2[0] + b1 - p2[1]) >= 0: # first appear in in_area
            return -1



f_cnt = 0
threashold = 0
people = 0
while True:
    f_cnt += 1
    frame, bounding_boxes, IDs, fps = framework.run_1_frame()
    for id in ID_Base.id_list:
        if id not in IDs:
            if (f_cnt - ID_Base.id_last_frame) > threashold:
                people += check(ID_Base.id_first[str(id)], ID_Base.id_last[str(id)], in_line, out_line)
                ID_Base.deleteID(id)

    ID_Base.updateID(bounding_boxes, IDs, f_cnt)



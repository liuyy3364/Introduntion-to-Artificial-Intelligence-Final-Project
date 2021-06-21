import Framework
import ID_Base
import numpy as np

# Solving following system of linear equation
# ax + b = y
# ex.(-2, 14), (4, -4)
# -2a + 1b = 14
# 4a + 1b = -4
# a = np.array([[-2, 1],[4,1]])
# b = np.array([14, -4])
# a, b = np.linalg.solve(a,b) // a=-3, b=8 
# y = -3x + 8

in_line = [(100, 0),(150, 30)] ##change
out_line = [(0, 90),(50 ,120)] ##change

def equation(line):
    a = int(line[0][0])
    b = int(line[0][1])
    c = int(line[1][0])
    d = int(line[1][1])

    n = np.array([[a, 1], [c,1]])
    m = np.array([b, d])
    a, b = np.linalg.solve(n, m)
    return a, b

def check(first, last, in_line, out_line):
    p1 = (first[0], first[1])
    p2 = (last[0], last[1])
    a1, b1 = equation(in_line)
    a2, b2 = equation(out_line)
    first_appear_out = (a2 * float(p1[0]) + b2 - float(p1[1]))
    first_appear_in = (a1 * float(p1[0]) + b1 - float(p1[1]))

    if (first_appear_out >= 0) and (first_appear_in <= 0): #appear in middle
        if (a2 * float(p2[0]) + b2 - float(p2[1])) <= 0: # last appear in out_area
            return 1
        elif (a1 * float(p2[0]) + b1 - float(p2[1])) >= 0: # last appear in in_area
            return -1
    elif first_appear_out >= 0: # first appear in in_area
        if (a2 * float(p2[0]) + b2 - float(p2[1])) <= 0: # last appear in out_area
            return 1
    elif first_appear_in <= 0: # first appear in out_area
        if (a1 * float(p2[0]) + b1 - float(p2[1])) >= 0: # last appear in in_area
            return -1
    return 0


fw = Framework.Framework()
fw.displayer.run()
idb = ID_Base()
f_cnt = 0
threashold = 10
people = 0
while True:
    f_cnt += 1
    frame, bounding_boxes, IDs, fps = fw.run_1_frame(draw = True)
    fw.displayer.update_frame(frame)
    for id in idb.id_list:
        if id not in IDs:
            if (f_cnt - idb.id_last_frame) > threashold:
                people += check(idb.id_first[str(id)], idb.id_last[str(id)], in_line, out_line)
                idb.deleteID(id)

    idb.updateID(bounding_boxes, IDs, f_cnt)

############### debug code #################
# inp = input()
# inp = inp.split()
# print(check((inp[0], inp[1]), (inp[2], inp[3]), in_line, out_line))



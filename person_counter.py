import Framework
import ID_Base
import numpy as np
import cv2

# Solving following system of linear equation
# ax + b = y
# ex.(-2, 14), (4, -4)
# -2a + 1b = 14
# 4a + 1b = -4
# a = np.array([[-2, 1],[4,1]])
# b = np.array([14, -4])
# a, b = np.linalg.solve(a,b) // a=-3, b=8 
# y = -3x + 8

in_line = [(768, 0),(1919, 100)] ##change
out_line = [(0, 90),(1919, 980)] ##change

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
            return 0
            # return -1
    elif first_appear_out >= 0: # first appear in in_area
        if (a2 * float(p2[0]) + b2 - float(p2[1])) <= 0: # last appear in out_area
            return 1
    elif first_appear_in <= 0: # first appear in out_area
        if (a1 * float(p2[0]) + b1 - float(p2[1])) >= 0: # last appear in in_area
            return 0
            # return -1
    return 0


fw = Framework.Framework()
fw.displayer.run()
idb = ID_Base.ID_Base()
f_cnt = 0
threashold = 10
people = 0
while True:
    f_cnt += 1
    frame, BB_IDs, fps = fw.run_1_frame(draw = True)
    cv2.line(frame, in_line[0], in_line[1],(255,0,0),2)
    cv2.line(frame, out_line[0], out_line[1],(255,0,0),2)
    cv2.putText(frame, str(people),(200,25), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
    fw.displayer.update_frame(frame)
    to_be_delete = []
    for id, info in idb.base.items():
        if id not in BB_IDs[:,4]:
            if (f_cnt - info.last_frame) > threashold:
                people += check(info.pos0, info.pos1, in_line, out_line)
                to_be_delete.append(id)

    for id in to_be_delete:
        idb.deleteID(id)
    idb.updateID(BB_IDs, f_cnt)
    print(people)

############### debug code #################
# inp = input()
# inp = inp.split()
# print(check((inp[0], inp[1]), (inp[2], inp[3]), in_line, out_line))



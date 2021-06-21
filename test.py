#301 working
#%%





# import cv2
# import torch
# from PIL import Image

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# # Images
# # for f in ['zidane.jpg', 'bus.jpg']:
#     # torch.hub.download_url_to_file('https://ultralytics.com/images/' + f, f)  # download 2 images


# # img1 = Image.open('zidane.jpg')  # PIL image
# img2 = cv2.imread('resources/FirstFrame.jpg')[:, :, ::-1]  # OpenCV image (BGR to RGB)
# # imgs = [img1, img2]  # batch of images

# # Inference
# results = model(img2)  # includes NMS

# # results.show()
# a = results.pandas().xyxy[0]

# for i, n in enumerate(a['name']):
#     if n == 'person':
#         a['xmin'][i]



# print(results.xyxy[0])
# print(results.xyxy[1])


# import time
# img = cv2.imread('resources/FirstFrame.jpg')
# t0=time.time()
# model(img)
# t1=time.time()
# print()





# import os 
# os.chdir("netadapt")# path to netadapt
# os.system("conda activate ")


# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# time.sleep(5)

# while True: 
    
#     ret,img=cap.read()
    
#     cv2.imshow('Video', img)
    
#     if(cv2.waitKey(10) & 0xFF == ord('b')):
#         break

#%%
# import cv2

# # 選擇第二隻攝影機
# cap = cv2.VideoCapture(0)

# while(True):
#   # 從攝影機擷取一張影像
#   ret, frame = cap.read()

#   # 顯示圖片
#   cv2.imshow('frame', frame)

#   # 若按下 q 鍵則離開迴圈
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# # 釋放攝影機
# cap.release()

# # 關閉所有 OpenCV 視窗
# cv2.destroyAllWindows()


#%%
# import cv2
# import torch
# from Detector import YOLOv5
# # frame = cv2.imread("C:\\Users\\ggurt\Desktop\\swKlRDl.png")
# detector = YOLOv5(interest_label='person')
# frame = cv2.imread("resources/FirstFrame.jpg")
# # boxes = [(50,50,100,100), (200,200,100,100)]
# boxes = detector.detect(frame)
# IDs = [x for x in range(300)]
# fps = 10
# cv2.rectangle(frame, (0, 0), (45, 12), (0, 0, 255), -1)
# cv2.putText(frame, "FPS "+str(fps), (1, 10), cv2.FONT_HERSHEY_TRIPLEX, 0.35, (0,0,0))
# for (x, y, w, h), id in zip(boxes, IDs):
#         # draw bounding box
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
#         # put id
#         cv2.rectangle(frame, (x, y-12), (x+21, y), (0, 0, 255), -1)
#         cv2.putText(frame, str(id), (x, y-2), cv2.FONT_HERSHEY_TRIPLEX, 0.35, (0,0,0))

# cv2.imshow("Image", frame)
# cv2.waitKey(0)
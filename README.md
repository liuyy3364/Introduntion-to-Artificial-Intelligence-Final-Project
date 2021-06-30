# Introduntion-to-Artificial-Intelligence-Final-Project

NYCU-2021-Spring-Introduntion-to-Artificial-Intelligence-Final-Project

## Target

做一個 Multiple Object Tracking (MOT) 的 framework，可以方便替換 Detector 和 Tracker，並有其他相關需要功能: benchmark 跟 optimize

最後我們在用這個 framework 做一個人流計算程式，像是用一個架在門口的攝影機就可以計算由這個入口進出的人數

## Intro

[簡介影片](https://drive.google.com/open?id=1ruZbwQpqmyh1VfMgaAaDVPoa49bqdHZi)
[5min版](https://drive.google.com/open?id=1ekAbpHO72SQ0FeWtcUqqgYgLcRrNw-ku)

## Component of framework

- Framework
    主程式

- Detector:
  - selected algorithm: opencv haar cascade and yolov5
  - input: frame
  - output: bounding boxes

- Tracker:
  - selected algorithm: SORT
  - input: bounding boxes
  - output: bounding boxes and assigned IDs

- Display
  - selected algorithm: Flask webserver with video stream
  - input: frame with bounding boxes with ID drawn on it
  - output: display input frame by somehow

- Benchmarker (abandoned)
  - input: MOT algorithm
  - output: performance metrics for MOT, e.g., MOTA, MOTP or FPS

- Optimizer
  - selected algorithm: Netadapt:
    - input: a pytorch model
    - output: a more efficient pytorch model

## Algorithm of people counter

- 將畫面分割為入口與出口及其他三區域
- 若發生以下事件，則更新人員進出淨值：
  - 有人從出口以外區域出現，並於出口消失，-1
  - 有人從入口以外區域出現，並於入口消失，+1
  
## Implementation of people counter

- 拿一張新的 frame
- Detect and track
- 記錄每個 ID 第一次出現在那個區域、最後一次出現在那個區域、最後一次出現的時間
- 檢查是否有 ID 的最後出現時間與現在時間差大於設定 threshold
  - 有: 依照第一次出現區域與最後一次出現區域，判斷是進入還是離開，並更新人員進出淨值
  - 無: continue

## Result

[影片連結](https://drive.google.com/open?id=1XU6IWtmS9EtDVjyI7nBtBGpsw_O3wCyD)

## Reference

[YOLOv5](https://github.com/ultralytics/yolov5)

[SORT](https://github.com/abewley/sort)

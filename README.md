# Introduntion-to-Artificial-Intelligence-Final-Project

NYCU-2021-Spring-Introduntion-to-Artificial-Intelligence-Final-Project

## 目標

做一個 Multiple Object Tracking (MOT) 的 framework，可以方便替換 Detector 和 Tracker，並有其他相關需要功能

## Part

- Detector
    input:frame
    output:bounding boxes

- Tracker
    input:frame
    output:assigned IDs

- Display
    input:frame
    output: display input frame by somehow

- Benchmarker
    反正就是做 benchmark input 自己訂
    output: performance metrics for MOT, e.g., MOTA(先這個就好) or MOTP or FPS(這個應該很簡單也做一下)

- Optimizer
    input: a pytorch model
    output: a more efficient pytorch model

自己fork之後認領下面的部分創PR
例：認領detector:

``` bash
#指令不一定對，傳達概念而已，自己調成對的
touch Detector.py
git add Detector.py
git commit -m "detector init commit"
git push
```

然後再丟 Pull Request 給我，接受後我的 Repo 就會有你認領的空檔了，自己認領前先注意有沒有已經存再在我的 branch 裡，開始做新檔案時先檢查有沒有被其他人認領過

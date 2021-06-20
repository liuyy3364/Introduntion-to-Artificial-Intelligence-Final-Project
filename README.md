# Introduntion-to-Artificial-Intelligence-Final-Project

NYCU-2021-Spring-Introduntion-to-Artificial-Intelligence-Final-Project

## 目標

做一個 Multiple Object Tracking (MOT) 的 framework，可以方便替換 Detector 和 Tracker，並有其他相關需要功能，目前先訂：benchmark 跟 optimize

最後我們在用這個 framework 做一個人流計算程式，像是用一個架在門口的攝影機就可以計算由這個入口進出的人數

## Part

這些部件都做成一個 class，init 自己做，在 comment 裡說明清楚就好
可以的話可以看一下 python 的 type hint 怎麼用，這裡給個範例：

``` python
class C():
    def init(self, arg1: int, arg2: list, arg3: type3) -> None:
        # arg1: arg1是幹什麼用的
        # arg2: arg2是幹什麼用的
        # arg3: arg3是幹什麼用的
        # ret_value: 回傳了什麼
        pass #未實作 pass能在呼叫時避免錯誤
        raise Exceptiom("發生exception") # 也可以選擇丟 exception ，這樣外面 call 的 func
    def return_int(self, arg1: str) -> int:
        return int(str)
```

各個部件用 open source 或自己寫

- Framework
    主程式

- Detector:
  - base-opencv haar cascade
  - advance-yoloV4
  - input:frame
  - output:bounding boxes

- Tracker:
  - base:opencv tracker
  - advance-SORT or DeepSORT
  - input:frame
  - output:assigned IDs

- Display
  - base:我打算用嵌入式系統的 flask 做 video stream，很簡單，翁要也行，記得不能在 main thread 跑，把 debug 設成 False 就能在 其他 thread app.start()了
  - advance: 有想到再考慮要不要，這部分沒那麼重要，其實有 base 就夠了
  - input:frame + bounding boxes with ID
  - output: display input frame by somehow

- Benchmarker
  - 反正就是做 benchmark input 自己訂
  - output: performance metrics for MOT, e.g., MOTA(先這個就好) or MOTP or FPS(這個應該很簡單也做一下)

- Optimizer (advance)
  - Netadapt:
    - input: a pytorch model
    - output: a more efficient pytorch model

- 算人數應用等全部做完再說

## 分工方式

自己fork之後認領上面的部件創 PR

例：認領detector:

``` bash
#指令不一定對，傳達概念而已，自己調成對的
touch Detector.py
git add Detector.py
git commit -m "detector init commit"
git push
```

然後再丟 Pull Request 給我，接受後我的 Repo 就會有你認領的空檔了，自己認領前先注意有沒有已經存再在我的 branch 裡，開始做新檔案時先檢查有沒有被其他人認領過

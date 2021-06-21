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
  - base: opencv haar cascade
  - advance: yolo
  - input: frame
  - output: bounding boxes

- Tracker:
  - base: opencv tracker
  - advance: SORT or DeepSORT
  - input: bounding boxes
  - output: assigned IDs

- Display
  - base: 我打算用嵌入式系統的 flask 做 video stream，很簡單，翁要也行，記得不能在 main thread 跑，把 debug 設成 False 就能在 其他 thread app.start()了
  - advance: 有想到再考慮要不要，這部分沒那麼重要，其實有 base 就夠了
  - input: frame + bounding boxes with ID
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

麻煩也把安裝的 module 列表也傳上來，執行了pip install就放進Requirement_ID末三碼.txt，可以參考一下我的，盡量同步一下環境，目前我用 python3.8，大家也用一下虛擬環境的程式來創一個乾淨的 python 3.8 環境

自己認領上面的部件，在該部件檔案的開頭加上自己的學號

例：認領detector:

``` bash
#指令不一定對，傳達概念而已，自己調成對的
echo "# 301" > Detector.py
git add Detector.py
git commit -m "detector init commit"
git push
```

之後我的 Repo 就會更新你認領的檔案了，認領前先注意有沒有其他人認領，認領完後記得 pull 一次，看開頭是不是真的是你的學號，是再繼續做，可以看 Optimizer 當範例

``` bash
# 認領完後
git pull
cat 認領.py
# output: # 301
# 開始實作
```

做完一個再認領下一個，如果那個部件需要一些本地資源，如 pre-trained model，創一個跟部件同名的資料夾，把需要的資源丟進去，超過 100 MB，就傳到 google drive 上，然後開對知道連結的人(不是僅限交大)的檢視者權限，然後把連結丟進去剛剛創的資料夾，順便寫在你的 requirement 裡

我會慢慢寫一些Template，再把template的class，複製一遍再改名字

## 補充 background

[MOT簡介](https://peaceful0907.medium.com/%E5%88%9D%E6%8E%A2%E7%89%A9%E4%BB%B6%E8%BF%BD%E8%B9%A4-multiple-object-tracking-mot-4f1b42e959f9)
[更詳細的但我覺得用不到看這麼細](https://www.zhihu.com/column/c_1102212337087401984)
[OpenCV padetrian detection](https://www.youtube.com/watch?v=LdlHEr6t45g)
[YOLOv5](https://github.com/ultralytics/yolov5) ，這是盜版yolo，因為不確定原本的repo是不是darknet，懶得爬，可以用其他的版本不一定要用這個
[OpenCV centroid tracker](https://www.youtube.com/watch?v=O3b8lVF93jU)
[DeepSORT](https://github.com/nwojke/deep_sort)
[SORT](https://github.com/abewley/sort)

# Granblue Fantasay - 古戰場修分
規劃古戰場修分方法的小工具

其他語言版本: [English](README.md), [中文](README.zh-tw.md)

![sample_result](assets/sample_result.png)

## Prerequisites
請至少讀過以下至少一篇教學以獲得了解如何穩定得取得想要的貢獻度。
- https://kamigame.jp/%E3%82%B0%E3%83%A9%E3%83%96%E3%83%AB/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88/%E6%B1%BA%E6%88%A6%EF%BC%81%E6%98%9F%E3%81%AE%E5%8F%A4%E6%88%A6%E5%A0%B4/%E8%B2%A2%E7%8C%AE%E5%BA%A6%E8%AA%BF%E6%95%B4.html
- https://gbf.wiki/User:Midokuni/Notepad/Beauty_of_Honor
- https://forum.gamer.com.tw/C.php?bsn=25204&snA=11313


## System requirements
- Python 3.7+


## Install requirements
You can use `pip` or `poetry` to install requirements.

### pip
```sh
$ pip install -r requirements.txt
```

### poetry
```sh
$ poetry install
```

## How to use
1. 打 hell boss 直到距離目標差距約一百萬貢獻。適當的差距可以讓我們有更大的機會找到一個比較容易達成的方式。
2. (WIP) (Optional) 調整 config
3. 執行 script 並根據提示輸入目前貢獻度及目標貢獻度

### Case 1: 直接找到答案
```python
$ python gbf_beautify_honors/main.py
Enter your current honors:  1398542611
Enter your expected honors: 1400000000
Need 1457389 honors.

Eyeball VH (0 button) = 3
Behemoth VH (0 button) = 7
Wicked Rebel EX (0 button) = 11
Wicked Rebel EX+ (0 button) = 6
Wicked Rebel EX+ (1 summon) = 3
Join raid and only use Break Assassin = 1
```

### Case 2: 無解
因為我們可以透過參加其他人的戰鬥並放如 BK 斬等技能來取得 1 貢獻，理論上一定有辦法達到任何貢獻。然而這並不是一個很實際的方法，所以預設的 config 有加上每種戰鬥最多可接受場數的限制。但這也導致了有時候會有無解的狀況發生

```
$ python gbf_beautify_honors/main.py
Enter your current honors:  1399999900
Enter your expected honors: 1400000000
Need 100 honors.

There is no solution to achieve the expected honors.
```

(WIP) 為了解決這個問題，我們可以調整 config 設定，放寬場數上限來找到解答。


## 原理
我們可以將完美調分視為一個整數規劃問題，並使用 [OR-Tools](https://developers.google.com/optimization) 來找到解答。

首先，我們定義 h<sub>i</sub> 為戰鬥 `i` (`i` 可以是 `VH 眼球關`, `EX+ 牛關`, ...) 可以得到的貢獻度。定義  n<sub>i</sub> 表示戰鬥 `i` 需要的場數。

我們想要以最少的場數 (最有效率) 來達到目標分數，所以對應的整數規劃問題如下：

<!-- Minimize\ \displaystyle\sum_{i} n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Minimize%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20n_i)

<!-- Subject\ to\ \displaystyle\sum_{i} h_i\times n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Subject%5C%20to%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20h_i%5Ctimes%20n_i%20%3D%20expected%5C_honor)

此外，我們可以加上額外的範圍限制到 n<sub>i</sub> 變數上以限制每種戰鬥最多可接受的場數。例如：

![formula](https://render.githubusercontent.com/render/math?math=0%3C%3Dn_i%3C%3D10)

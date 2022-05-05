# Granblue Fantasay - 古戰場修分

![PyPI - Package Version](https://img.shields.io/pypi/v/gbf-beautify-honors)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gbf-beautify-honors)
![PyPI - Status](https://img.shields.io/pypi/status/gbf-beautify-honors)
![PyPI - License](https://img.shields.io/pypi/l/gbf-beautify-honors)

規劃古戰場修分方法的 CLI 小工具

其他語言版本: [English](README.md), [中文](README.zh-tw.md)

<!-- a hack for pypi homepage shoing assets/sample_result.png -->
![sample_result](https://raw.githubusercontent.com/qq88976321/gbf-beautify-honors/master/assets/sample_result.png)

## Table of contents
<!--ts-->
* [Granblue Fantasay - 古戰場修分](README.zh-tw.md#granblue-fantasay---古戰場修分)
   * [Table of contents](README.zh-tw.md#table-of-contents)
   * [Prerequisites](README.zh-tw.md#prerequisites)
   * [System requirements](README.zh-tw.md#system-requirements)
   * [How to install](README.zh-tw.md#how-to-install)
   * [How to use](README.zh-tw.md#how-to-use)
      * [Interactive mode example](README.zh-tw.md#interactive-mode-example)
      * [Direct mode example](README.zh-tw.md#direct-mode-example)
   * [Examples](README.zh-tw.md#examples)
      * [Case 1: 直接找到答案](README.zh-tw.md#case-1-直接找到答案)
      * [Case 2: 無解](README.zh-tw.md#case-2-無解)
   * [原理](README.zh-tw.md#原理)
<!--te-->

## Prerequisites

請至少讀過以下至少一篇教學以獲得了解如何穩定得取得想要的貢獻度。

- [kamigame - 古戦場の貢献度調整のやり方](https://kamigame.jp/%E3%82%B0%E3%83%A9%E3%83%96%E3%83%AB/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88/%E6%B1%BA%E6%88%A6%EF%BC%81%E6%98%9F%E3%81%AE%E5%8F%A4%E6%88%A6%E5%A0%B4/%E8%B2%A2%E7%8C%AE%E5%BA%A6%E8%AA%BF%E6%95%B4.html)
- [gbf.wiki - Beauty of Honor](https://gbf.wiki/User:Midokuni/Notepad/Beauty_of_Honor)
- [巴哈姆特 - 古戰場修分大法(控分技巧)](https://forum.gamer.com.tw/C.php?bsn=25204&snA=11313)

## System requirements

- Python 3.7+

## How to install

建議使用 [pipx](https://pypa.github.io/pipx/) 來進行安裝，pipx 會將此工具安裝在一個獨立且乾淨的環境內。

```sh
pipx install gbf-beautify-honors
```

然而，仍然可以使用 pip 進行安裝。

```sh
pip install gbf-beautify-honors
```

## How to use

1. 打 hell boss 直到距離目標差距約一百萬貢獻。適當的差距可以讓我們有更大的機會找到一個比較容易達成的方式。
2. 以 interactive mode 或 direct mode 執行 cli tool，以下是這個 tool 的 help page:

```sh
$ gbf-beautify-honors --help
Usage: gbf-beautify-honors [OPTIONS]

Options:
  --current INTEGER   Your current honors  [required]
  --expected INTEGER  Your expected honors  [required]
  --config PATH       Custom config path
  --help              Show this message and exit.
```

### Interactive mode example

```sh
$ gbf-beautify-honors
Your current honors : 1398542611
Your expected honors: 1400000000
Custom config path []:
```

### Direct mode example

```sh
gbf-beautify-honors --current=1398542611 --expected=1400000000
```

## Examples

接下來，我們使用幾個範例來說明如何使用這個工具，以及如何調整設定檔案。

### Case 1: 直接找到答案

```sh
$ gbf-beautify-honors
Your current honors : 1398542611
Your expected honors: 1400000000
Custom config path []:
╒═══════════════════════════════════════╤═════════╤═════════════════╕
│ Action                                │   Honor │   Optimal Times │
╞═══════════════════════════════════════╪═════════╪═════════════════╡
│ Eyeball VH (0 button)                 │    8000 │               1 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast VH (0 button)              │   21400 │               4 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast EX (0 button)              │   50578 │               3 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast EX+ (0 button)             │   80800 │              10 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast EX+ (1 summon)             │   80810 │               5 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Join raid and only use Break Assassin │       1 │               5 │
╘═══════════════════════════════════════╧═════════╧═════════════════╛
```

請注意同一個問題可能有多種解答，且目前不保證每次結果的一致性。另一種可能性如下所示：

```sh
$ gbf-beautify-honors
Your current honors : 1398542611
Your expected honors: 1400000000
Custom config path []:
╒═══════════════════════════════════════╤═════════╤═════════════════╕
│ Action                                │   Honor │   Optimal Times │
╞═══════════════════════════════════════╪═════════╪═════════════════╡
│ Eyeball H (0 button)                  │    6000 │               3 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Eyeball VH (0 button)                 │    8000 │               3 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast VH (0 button)              │   21400 │               1 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast EX (0 button)              │   50578 │               2 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast EX+ (0 button)             │   80800 │              13 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Meat Beast EX+ (1 summon)             │   80810 │               3 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Join raid and only use Break Assassin │       1 │               3 │
╘═══════════════════════════════════════╧═════════╧═════════════════╛
```

### Case 2: 無解

因為我們可以透過參加其他人的戰鬥並放如 BK 斬等技能來取得 1 貢獻，理論上一定有辦法達到任何貢獻。然而這並不是一個很實際的方法，所以預設的 config 有加上每種戰鬥最多可接受場數的限制。但這也導致了有時候會有無解的狀況發生

```sh
$ gbf-beautify-honors
Your current honors : 1399999900
Your expected honors: 1400000000
Custom config path []:
There is no solution to achieve the expected honors. Please relax the constraints and try again.
```

為了解決這個問題，我們可以調整 config 設定，放寬限制來找到解答。

1. 下載範例的 [config.json](example_configs/config.json) 或中文版本的 [config.zh-tw.json](example_configs/config.zh-tw.json)。
2. 修改 "Join raid and only use Break Assassin" action 的 `max_acceptable_times` 為 `100`。
3. 以客製化的設定檔再次執行工具。
<!-- FIXME: double-width characters alignment issue when using chinese? -->
```sh
$ gbf-beautify-honors
Your current honors : 1399999900
Your expected honors: 1400000000
Custom config path []: config.json
╒═══════════════════════════════════════╤═════════╤═════════════════╕
│ Action                                │   Honor │   Optimal Times │
╞═══════════════════════════════════════╪═════════╪═════════════════╡
│ Join raid and only use Break Assassin │       1 │             100 │
╘═══════════════════════════════════════╧═════════╧═════════════════╛
```

設定檔的配置是很靈活的，你可以嘗試調整設定檔內不同的數值，重新執行並確認是否有解。如果你發現某些自定義的行為可以穩定得獲得特定貢獻度，你也可以將其加入到設定檔內。例如：你可以試著將下列物件加入 `actions` list 中

```json
{
    "name": "Some custom action for demo",
    "honor": 11,
    "max_acceptable_times": 10
}
```

再次執行工具可以看到他正常運作

```sh
$ gbf-beautify-honors
Your current honors : 1399999900
Your expected honors: 1400000000
Custom config path []: config.json
╒═══════════════════════════════════════╤═════════╤═════════════════╕
│ Action                                │   Honor │   Optimal Times │
╞═══════════════════════════════════════╪═════════╪═════════════════╡
│ Join raid and only use Break Assassin │       1 │               1 │
├───────────────────────────────────────┼─────────┼─────────────────┤
│ Some custom action for demo           │      11 │               9 │
╘═══════════════════════════════════════╧═════════╧═════════════════╛
```

## 原理

我們可以將完美調分視為一個整數規劃問題，並使用 [OR-Tools](https://developers.google.com/optimization) 來找到解答。

首先，我們定義 h<sub>i</sub> 為戰鬥 `i` (`i` 可以是 `VH 眼球關`, `EX+ 牛關`, ...) 可以得到的貢獻度。定義  n<sub>i</sub> 表示戰鬥 `i` 需要的場數。

我們想要以最少的場數 (最有效率) 來達到目標分數，所以對應的整數規劃問題如下：

<!-- Minimize\ \displaystyle\sum_{i} n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Minimize%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20n_i)

<!-- Subject\ to\ \displaystyle\sum_{i} h_i\times n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Subject%5C%20to%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20h_i%5Ctimes%20n_i%20%3D%20expected%5C_honor)

此外，我們可以加上額外的範圍限制到 n<sub>i</sub> 變數上以限制每種戰鬥最多可接受的場數。例如：

![formula](https://render.githubusercontent.com/render/math?math=0%E2%89%A4n_i%E2%89%A410)

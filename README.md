# Granblue Fantasay - Beautify Honors
A tool to help you figure out how to beautify honors in the Guild War event. (古戦場の貢献度調整)

Read this in other languages: [English](README.md), [中文](README.zh-tw.md).


![sample_result](assets/sample_result.png)

## Prerequisites
Please read at least one of these well-written tutorials to known how to get the exact honors.
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

1. Solo the NM Bosses until the difference between your current honors and expected honors is roughly greater than one million. An appropriate gap is a good start because there may be a greater chance of finding a good way to achieve the goal.
2. (WIP) (Optional) Edit the config.
3. Run the script and enter your current honors and expected honors.

### Case 1: There is a solution
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

### Case 2: There is no solution
Basically, there is always a solution because we can join raid and only use Break Assassin to get exactly 1 honor.
However, this is usually an unrealistic approach, so the default config makes some constraints on the maximum time on each type of battle. This leads to the fact that sometimes it is not possible to find a solution.
```
$ python gbf_beautify_honors/main.py
Enter your current honors:  1399999900
Enter your expected honors: 1400000000
Need 100 honors.

There is no solution to achieve the expected honors.
```

(WIP) To solve this problem, we can adjust the settings to relax the constraints to find a solution.



## How it works
We can formulate this problem as an integer programming problem and solve it using the [OR-Tools](https://developers.google.com/optimization)

Is this case, we use an integer variable h<sub>i</sub> to represent the exact honor earned from battle `i` (`i` can be `Eyeball N`, `Wicked Rebel EX+`, ...).
And use another integer variable n<sub>i</sub> to represent the number of battles we need to fight for the battle `i`.

We want to get exact honors with minimum number of battles (more efficient), so the corresponding integer programming problem is:

<!-- Minimize\ \displaystyle\sum_{i} n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Minimize%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20n_i)

<!-- Subject\ to\ \displaystyle\sum_{i} h_i\times n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Subject%5C%20to%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20h_i%5Ctimes%20n_i%20%3D%20expected%5C_honor)

Additionally, we can add additional constriants to the integer variable n<sub>i</sub> to limit the maximum number of each battle. e.g.,

![formula](https://render.githubusercontent.com/render/math?math=0%3C%3Dn_i%3C%3D10)


## How to develop
### Setup
Use `poetry` to setup dev environment.
```sh
$ poetry install
$ poetry shell
```

Use `pre-commit` hook to check coding style.
```sh
$ pre-commit install -t commit-msg -t pre-commit
```

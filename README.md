# Granblue Fantasy - Beautify Honors

![PyPI - Package Version](https://img.shields.io/pypi/v/gbf-beautify-honors)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gbf-beautify-honors)
![PyPI - Status](https://img.shields.io/pypi/status/gbf-beautify-honors)
![PyPI - License](https://img.shields.io/pypi/l/gbf-beautify-honors)

A CLI tool to help you figure out how to beautify honors in the Guild War event. (古戦場の貢献度調整)

Read this in other languages: [English](README.md), [中文](README.zh-tw.md).

<!-- a hack for pypi homepage showing assets/sample_result.png -->
![sample_result](https://raw.githubusercontent.com/qq88976321/gbf-beautify-honors/master/assets/sample_result.png)

## Table of contents
<!--ts-->
* [Granblue Fantasay - Beautify Honors](README.md#granblue-fantasay---beautify-honors)
   * [Table of contents](README.md#table-of-contents)
   * [Prerequisites](README.md#prerequisites)
   * [System requirements](README.md#system-requirements)
   * [How to install](README.md#how-to-install)
   * [How to use](README.md#how-to-use)
      * [Interactive mode example](README.md#interactive-mode-example)
      * [Direct mode example](README.md#direct-mode-example)
   * [Examples](README.md#examples)
      * [Case 1: There is a solution](README.md#case-1-there-is-a-solution)
      * [Case 2: There is no solution](README.md#case-2-there-is-no-solution)
   * [How it works](README.md#how-it-works)
   * [How to develop](README.md#how-to-develop)
      * [Setup](README.md#setup)
<!--te-->

## Prerequisites

Please read at least one of these well-written tutorials to known how to get the exact honors.

- [kamigame - 古戦場の貢献度調整のやり方](https://kamigame.jp/%E3%82%B0%E3%83%A9%E3%83%96%E3%83%AB/%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88/%E6%B1%BA%E6%88%A6%EF%BC%81%E6%98%9F%E3%81%AE%E5%8F%A4%E6%88%A6%E5%A0%B4/%E8%B2%A2%E7%8C%AE%E5%BA%A6%E8%AA%BF%E6%95%B4.html)
- [gbf.wiki - Beauty of Honor](https://gbf.wiki/User:Midokuni/Notepad/Beauty_of_Honor)
- [巴哈姆特 - 古戰場修分大法(控分技巧)](https://forum.gamer.com.tw/C.php?bsn=25204&snA=11313)

## System requirements

- Python 3.7+

## How to install

It is recommended to use [pipx](https://pypa.github.io/pipx/) to install this tool because the application will be installed into an isolated and clean environment.

```sh
pipx install gbf-beautify-honors
```

However, you still can use pip to install this cli.

```sh
pip install gbf-beautify-honors
```

## How to use

1. Solo the NM Bosses until the difference between your current honors and expected honors is roughly greater than one million. An appropriate gap is a good start because there may be a greater chance of finding a good way to achieve the goal.
2. Run the cli tool in interactive mode or direct mode. Help page is simply shown below:

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

Next, we will use some examples to explain how to use this tool, and how to adjust the configuration file.

### Case 1: There is a solution

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

Please note that there may be multiple solutions to the same input and there is currently no guarantee of consistent results. Another possibility is shown below:

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

### Case 2: There is no solution

Basically, there is always a solution because we can join raid and only use Break Assassin to get exactly 1 honor.
However, this is usually an unrealistic approach, so the default config makes some constraints on the maximum time on each type of battle. This leads to the fact that sometimes it is not possible to find a solution.

```sh
$ gbf-beautify-honors
Your current honors : 1399999900
Your expected honors: 1400000000
Custom config path []:
There is no solution to achieve the expected honors. Please relax the constraints and try again.
```

To solve this problem, we can use custom config to relax the constraints to find a solution.

1. Download the example [config.json](example_configs/config.json).
2. Modify the `max_acceptable_times` of the action "Join raid and only use Break Assassin" to `100`.
3. Re-run the script with custom config.

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

The configuration is flexible and you can try to modify different values in it, re-run the script and see if there is a solution. You can also add self-defined action into the config.json as long as you know you can get the exact honor value from this action, e.g. you can add this object into the actions list,

```json
{
    "name": "Some custom action for demo",
    "honor": 11,
    "max_acceptable_times": 10
}
```

Re-run the script, it just works!

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

## How it works

We can formulate this problem as an integer programming problem and solve it using the [OR-Tools](https://developers.google.com/optimization)

Is this case, we use an integer variable h<sub>i</sub> to represent the exact honor earned from battle `i` (`i` can be `Eyeball N`, `Meat Beast EX+`, ...).
And use another integer variable n<sub>i</sub> to represent the number of battles we need to fight for the battle `i`.

We want to get exact honors with minimum number of battles (more efficient), so the corresponding integer programming problem is:

<!-- Minimize\ \displaystyle\sum_{i} n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Minimize%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20n_i)

<!-- Subject\ to\ \displaystyle\sum_{i} h_i\times n_i -->
![formula](https://render.githubusercontent.com/render/math?math=Subject%5C%20to%5C%20%5Cdisplaystyle%5Csum_%7Bi%7D%20h_i%5Ctimes%20n_i%20%3D%20expected%5C_honor)

Additionally, we can add additional constraints to the integer variable n<sub>i</sub> to limit the maximum number of each battle. e.g.,

![formula](https://render.githubusercontent.com/render/math?math=0%E2%89%A4n_i%E2%89%A410)

## How to develop

### Setup

Use `poetry` to setup dev environment.

```sh
poetry install
poetry shell
```

Use `pre-commit` hook to check coding style.

```sh
pre-commit install -t commit-msg -t pre-commit
```

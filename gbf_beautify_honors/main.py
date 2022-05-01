#!/usr/bin/env python3
from ortools.init import pywrapinit

from gbf_beautify_honors.action import Actions
from gbf_beautify_honors.solver import solve


def main():
    try:
        current_honors = int(input("Enter your current honors:  "))
        expected_total_honors = int(input("Enter your expected honors: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    expected_honors = expected_total_honors - current_honors
    print(f"Need {expected_honors} honors.\n")

    # TODO: read config or use default settings
    actions = Actions()

    if solve(actions, expected_honors):
        print(actions)


def init_or_tools():
    pywrapinit.CppBridge.InitLogging("main.py")
    cpp_flags = pywrapinit.CppFlags()
    cpp_flags.logtostderr = True
    cpp_flags.log_prefix = False
    pywrapinit.CppBridge.SetFlags(cpp_flags)


if __name__ == "__main__":
    init_or_tools()
    main()

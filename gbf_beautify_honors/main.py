#!/usr/bin/env python3
import json

import click
from ortools.init import pywrapinit

from gbf_beautify_honors.action import Actions
from gbf_beautify_honors.solver import solve


@click.command()
@click.option(
    "--current",
    "current_honors",
    prompt="Your current honors ",
    required=True,
    type=int,
    help="Your current honors",
)
@click.option(
    "--expected",
    "expected_honors",
    prompt="Your expected honors",
    required=True,
    type=int,
    help="Your expected honors",
)
@click.option(
    "--config",
    "custom_config_path",
    prompt="Custom config path",
    required=False,
    type=click.Path(),
    help="Custom config path",
    default="",
)
def main(current_honors, expected_honors, custom_config_path):
    init_or_tools()

    actions = Actions()

    # read custom config into actions object if needed
    if custom_config_path:
        with open(custom_config_path) as f:
            actions_dict = json.load(f)
            actions = Actions.from_dict(actions_dict)  # type: ignore

    honors_diff = expected_honors - current_honors

    solve(actions, honors_diff)


def init_or_tools():
    pywrapinit.CppBridge.InitLogging("main.py")
    cpp_flags = pywrapinit.CppFlags()
    cpp_flags.logtostderr = True
    cpp_flags.log_prefix = False
    pywrapinit.CppBridge.SetFlags(cpp_flags)


if __name__ == "__main__":
    main()

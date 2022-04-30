#!/usr/bin/env python3

from typing import Dict, Tuple

from ortools.init import pywrapinit
from ortools.linear_solver import pywraplp


def fine_fune_honors(battle_honor_dict: Dict[str, Tuple[int, int]], expected_honors: int) -> None:
    """Find an optimal way (if any) to achieve the expected honors with given battles.

    Args:
        battle_honor_dict (Dict[str, Tuple[int, int]]): battle related infomation
            key: battle name
            value: tuple of (honor, the maximum acceptable number of this battle)
        expected_honors (int): how many honors you want to get
    """
    solver = pywraplp.Solver.CreateSolver(solver_id="SAT")

    # Define the objective: achieve our expected honors with minimum battles.
    objective = solver.Objective()

    # Define the constraint: expected_total_honors equals sum of each battle's (times * honor)
    # The first two arguments to the method are the lower and upper bounds for the constraint.
    constraint = solver.RowConstraint(expected_honors, expected_honors)

    variable_list = []
    for battle_name, (honor, max_acceptable_battles) in battle_honor_dict.items():
        variable = solver.IntVar(0, max_acceptable_battles, battle_name)
        variable_list.append(variable)
        objective.SetCoefficient(variable, 1)
        constraint.SetCoefficient(variable, honor)

    objective.SetMinimization()

    # Solve the problem and print the solution.
    result_status = solver.Solve()

    # The problem has an optimal solution.
    if result_status != pywraplp.Solver.OPTIMAL:
        print("There is no solution to achieve the expected honors. Please relax the constraints and try again.")
        return

    # The solution looks legit (when using solvers others than
    # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
    try:
        assert solver.VerifySolution(1e-7, True)
    except AssertionError:
        print("Invalid solution. Please try again.")
        return

    # The value of each variable in the solution.
    for variable in variable_list:
        if variable.solution_value() > 0:
            print(f"{variable.name()} = {variable.solution_value():.0f}")


def main():
    try:
        current_honors = int(input("Enter your current honors:  "))
        expected_total_honors = int(input("Enter your expected honors: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    expected_honors = expected_total_honors - current_honors
    print(f"Need {expected_honors} honors.\n")

    # common value for maximum accepatble battles
    max_acceptable_battles = 50

    # IMPORTANT: The honor shown below is for one turn kill without using skills and summons
    #            Special case: we have more chances to find the solution if we use sommon or skill
    # key: battle name
    # value: (honor, the maximum acceptable number of this battle)
    battle_honor_dict: Dict[str, Tuple[int, int]] = {
        "Eyeball N (0 button)": (4000, max_acceptable_battles),
        "Eyeball H (0 button)": (6000, max_acceptable_battles),
        "Eyeball VH (0 button)": (8000, max_acceptable_battles),
        "Behemoth VH (0 button)": (21400, max_acceptable_battles),
        "Wicked Rebel EX (0 button)": (50578, max_acceptable_battles),
        "Wicked Rebel EX+ (0 button)": (80800, max_acceptable_battles),
        # special case: use one summon can get 10 more honors
        "Wicked Rebel EX+ (1 summon)": (80800 + 10, max_acceptable_battles),
        # special case: some skills like break assasin that do not affect other players can get 1 honor
        "Join raid and only use Break Assassin": (1, 10),
    }

    fine_fune_honors(battle_honor_dict, expected_honors)


def init_or_tools():
    pywrapinit.CppBridge.InitLogging("tune_total_honors.py")
    cpp_flags = pywrapinit.CppFlags()
    cpp_flags.logtostderr = True
    cpp_flags.log_prefix = False
    pywrapinit.CppBridge.SetFlags(cpp_flags)


if __name__ == "__main__":
    init_or_tools()
    main()

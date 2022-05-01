#!/usr/bin/env python3
from typing import List

from ortools.init import pywrapinit
from ortools.linear_solver import pywraplp
from tabulate import tabulate


class Action:
    def __init__(self, name: str, honor: int, max_accepatable_times: int):
        self.name = name
        self.honor = honor
        self.max_accepatable_times = max_accepatable_times
        self.optimal_times = None


def fine_fune_honors(actions: List[Action], expected_honors: int) -> bool:
    """Find an optimal way (if any) to achieve the expected honors with given battles.

    Args:
        actions (List[Action]): action related information
        expected_honors (int): how many honors you want to get

    Returns:
        bool: find solution or not
    """
    solver = pywraplp.Solver.CreateSolver(solver_id="SAT")

    # Define the objective: achieve our expected honors with minimum battles.
    objective = solver.Objective()

    # Define the constraint: expected_total_honors equals sum of each battle's (times * honor)
    # The first two arguments to the method are the lower and upper bounds for the constraint.
    constraint = solver.RowConstraint(expected_honors, expected_honors)

    variable_list = []
    for action in actions:
        variable = solver.IntVar(0, action.max_accepatable_times, action.name)
        variable_list.append(variable)
        objective.SetCoefficient(variable, 1)
        constraint.SetCoefficient(variable, action.honor)

    objective.SetMinimization()

    # Solve the problem and print the solution.
    result_status = solver.Solve()

    # The problem has an optimal solution.
    if result_status != pywraplp.Solver.OPTIMAL:
        print("There is no solution to achieve the expected honors. Please relax the constraints and try again.")
        return False

    # The solution looks legit (when using solvers others than
    # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
    if not solver.VerifySolution(1e-7, True):
        print("The solution returned by the solver violated the problem constraints by at least 1e-7. Please try again.")
        return False

    # The value of each variable in the solution.
    for (i, variable) in enumerate(variable_list):
        actions[i].optimal_times = variable.solution_value()

    return True


def print_actions(actions: List[Action]):
    print(
        tabulate(
            [[a.name, a.honor, a.optimal_times] for a in actions],
            ["Action", "Honor", "Optimal Times"],
            tablefmt="fancy_grid",
        )
    )


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

    actions = [
        Action("Eyeball N (0 button)", 4000, max_acceptable_battles),
        Action("Eyeball H (0 button)", 6000, max_acceptable_battles),
        Action("Eyeball VH (0 button)", 8000, max_acceptable_battles),
        Action("Meat Beast VH (0 button)", 21400, max_acceptable_battles),
        Action("Meat Beast EX (0 button)", 50578, max_acceptable_battles),
        Action("Meat Beast EX+ (0 button)", 80800, max_acceptable_battles),
        # special case: use one summon can get 10 more honors
        Action("Meat Beast EX+ (1 summon)", 80800 + 10, max_acceptable_battles),
        # special case: some skills like break assasin that do not affect other players can get 1 honor
        Action("Join raid and only use Break Assassin", 1, 10),
    ]

    if fine_fune_honors(actions, expected_honors):
        print_actions(actions)


def init_or_tools():
    pywrapinit.CppBridge.InitLogging("main.py")
    cpp_flags = pywrapinit.CppFlags()
    cpp_flags.logtostderr = True
    cpp_flags.log_prefix = False
    pywrapinit.CppBridge.SetFlags(cpp_flags)


if __name__ == "__main__":
    init_or_tools()
    main()

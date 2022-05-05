from ortools.linear_solver import pywraplp

from gbf_beautify_honors.action import Actions, OptimalAction, OptimalActions
from gbf_beautify_honors.exception import NoSolutionError


def solve(actions: Actions, honors_diff: int) -> OptimalActions:
    """Find an optimal way (if any) to achieve the expected honors with given battles.

    Args:
        actions (List[Action]): action related information
        honors_diff (int): how many honors we need to get
    """
    solver = pywraplp.Solver.CreateSolver(solver_id="SAT")
    optimal_action_list = []

    # Define the objective: achieve our expected honors with minimum battles.
    objective = solver.Objective()

    # Define the constraint: expected_total_honors equals sum of each battle's (times * honor)
    # The first two arguments to the method are the lower and upper bounds for the constraint.
    constraint = solver.RowConstraint(honors_diff, honors_diff)

    variable_list = []
    for action in actions:
        variable = solver.IntVar(0, action.max_acceptable_times, action.name)
        variable_list.append(variable)
        objective.SetCoefficient(variable, 1)
        constraint.SetCoefficient(variable, action.honor)

    objective.SetMinimization()

    # Solve the problem and print the solution.
    result_status = solver.Solve()

    # The problem has an optimal solution.
    if result_status != pywraplp.Solver.OPTIMAL:
        raise NoSolutionError("There is no solution to achieve the expected honors. Please relax the constraints and try again.")

    # The solution looks legit (when using solvers others than
    # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
    if not solver.VerifySolution(1e-7, True):
        raise NoSolutionError("The solution returned by the solver violated the problem constraints by at least 1e-7. Please try again.")

    # The value of each variable in the solution.
    for i, variable in enumerate(variable_list):
        optimal_action_list.append(OptimalAction(actions[i].name, actions[i].honor, actions[i].max_acceptable_times, variable.solution_value()))

    return OptimalActions(optimal_action_list)

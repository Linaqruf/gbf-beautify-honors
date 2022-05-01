from ortools.linear_solver import pywraplp

from gbf_beautify_honors.action import Actions


def solve(actions: Actions, expected_honors: int) -> bool:
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
        print(
            "The solution returned by the solver violated the problem constraints by at least 1e-7. Please try again."
        )
        return False

    # The value of each variable in the solution.
    for (i, variable) in enumerate(variable_list):
        actions[i].optimal_times = variable.solution_value()

    return True

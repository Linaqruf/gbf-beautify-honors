from dataclasses import dataclass, field
from typing import List

from tabulate import tabulate


@dataclass
class Action:
    name: str
    honor: int
    max_accepatable_times: int
    optimal_times: int = field(init=False)


@dataclass
class Actions:
    actions: List[Action] = field(
        default_factory=lambda: [
            # IMPORTANT: The honor shown below is for one turn kill without using skills and summons
            #            Special case: we have more chances to find the solution if we use sommon or skill
            Action("Eyeball N (0 button)", 4000, 10),
            Action("Eyeball H (0 button)", 6000, 10),
            Action("Eyeball VH (0 button)", 8000, 10),
            Action("Meat Beast VH (0 button)", 21400, 50),
            Action("Meat Beast EX (0 button)", 50578, 50),
            Action("Meat Beast EX+ (0 button)", 80800, 50),
            # special case: use one summon can get 10 more honors
            Action("Meat Beast EX+ (1 summon)", 80800 + 10, 50),
            # special case: some skills like break assasin that do not affect other players can get 1 honor
            Action("Join raid and only use Break Assassin", 1, 10),
        ]
    )

    def __iter__(self):
        return iter(self.actions)

    def __getitem__(self, index):
        return self.actions[index]

    def __str__(self):
        return tabulate(
            [[action.name, action.honor, action.optimal_times] for action in self.actions if action.optimal_times != 0],
            ["Action", "Honor", "Optimal Times"],
            tablefmt="fancy_grid",
        )

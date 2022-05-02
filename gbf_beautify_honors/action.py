from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json
from tabulate import tabulate


@dataclass_json
@dataclass
class Action:
    name: str
    honor: int
    max_accepatable_times: int
    optimal_times: int = field(init=False)


@dataclass_json
@dataclass
class Actions:
    actions: List[Action] = field(default_factory=list)

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

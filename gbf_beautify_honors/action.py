from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json
from tabulate import tabulate


@dataclass_json
@dataclass
class Action:
    name: str
    honor: int
    max_acceptable_times: int


@dataclass_json
@dataclass
class Actions:
    actions: List[Action] = field(default_factory=list)

    def __iter__(self):
        return iter(self.actions)

    def __getitem__(self, index):
        return self.actions[index]


@dataclass
class OptimalAction(Action):
    optimal_times: int


@dataclass
class OptimalActions:
    optimal_actions: List[OptimalAction] = field(default_factory=list)

    def __iter__(self):
        return iter(self.optimal_actions)

    def __getitem__(self, index):
        return self.optimal_actions[index]

    def pretty_print(self):
        print(
            tabulate(
                [[action.name, action.honor, action.optimal_times] for action in self.optimal_actions if action.optimal_times != 0],
                ["Action", "Honor", "Optimal Times"],
                tablefmt="fancy_grid",
            )
        )

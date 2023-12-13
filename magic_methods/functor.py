from typing import Any


class RobotSteps:
    def __init__(self, initial) -> None:
        self.steps = initial
    
    def __call__(self, step) -> Any:
        self.steps += step
        return self
    
steps = RobotSteps(3)
print(steps.steps)
steps(13)(1)
print(steps.steps)


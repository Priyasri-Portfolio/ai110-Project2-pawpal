from dataclasses import dataclass, field
from typing import List

@dataclass
class Owner:
    name: str
    pets: List['Pet'] = field(default_factory=list)

@dataclass
class Pet:
    name: str
    type: str
    age: int
    #1)step 5)added after asking copilot to check on the skeleton, initially not added
    tasks: List['Task'] = field(default_factory=list)

    def __post_init__(self):
        #1)step 5)added after asking copilot to check on the skeleton, initially not added
        if self.age < 0:
            raise ValueError("Age must be non-negative")

@dataclass
class Task:
    name: str
    duration: int
    priority: int
    #1)step 5)this method was added after asked Copilot to check on the skeleton
    def __post_init__(self):
        if self.duration <= 0:
            raise ValueError("Duration must be positive")
        if self.priority < 1:
            raise ValueError("Priority must be at least 1")

    def __str__(self):
        return f"{self.name} ({self.duration} min, priority {self.priority})"
#1)step 5)this class was modeified after asked copilot to check on the skeleton.
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.tasks = self._get_all_tasks()

    def _get_all_tasks(self) -> List[Task]:
        """Collect all tasks from the owner's pets."""
        all_tasks = []
        for pet in self.owner.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def sort_tasks_by_priority(self):
        """Sort tasks by priority (higher first)."""
        self.tasks.sort(key=lambda t: t.priority, reverse=True)

    def generate_plan(self, available_time: int) -> List[Task]:
        """Return a list of tasks that fit within the available time, prioritized by priority."""
        self.sort_tasks_by_priority()
        plan = []
        total_time = 0
        for task in self.tasks:
            if total_time + task.duration <= available_time:
                plan.append(task)
                total_time += task.duration
            else:
                break
        return plan


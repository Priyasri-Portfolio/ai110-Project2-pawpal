from dataclasses import dataclass
from typing import List

@dataclass
class Owner:
    name: str


@dataclass
class Pet:
    name: str
    type: str
    age: int


@dataclass
class Task:
    name: str
    duration: int
    priority: int

    def __str__(self):
        return f"{self.name} ({self.duration} min, priority {self.priority})"


class Scheduler:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def sort_tasks_by_priority(self):
        """Sort tasks by priority (higher first)."""
        pass  # logic added in Phase 2

    def generate_plan(self, available_time: int):
        """Return a list of tasks that fit within the available time."""
        pass  # logic added in Phase 2

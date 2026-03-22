from dataclasses import dataclass, field
from typing import List

@dataclass
class Owner:
    name: str
    pets: List['Pet'] = field(default_factory=list)

    def add_pet(self, pet: 'Pet'):
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)

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
    #2)step1)
    def add_task(self, task: 'Task'):
        """Add a task to the pet's list of tasks."""
        self.tasks.append(task)

@dataclass
class Task:
    name: str
    duration: int
    priority: int
    frequency: str = "daily"
    completed: bool = False

    def __post_init__(self):
        if self.duration <= 0:
            raise ValueError("Duration must be positive")
        if self.priority < 1:
            raise ValueError("Priority must be at least 1")

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.name} ({self.duration} min, priority {self.priority}, {status})"

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
        # Retrieve fresh tasks each time to account for any additions after Scheduler creation
        tasks = self._get_all_tasks()
        tasks.sort(key=lambda t: t.priority, reverse=True)
        plan = []
        total_time = 0
        for task in tasks:
            if total_time + task.duration <= available_time:
                plan.append(task)
                total_time += task.duration
            else:
                break
        return plan

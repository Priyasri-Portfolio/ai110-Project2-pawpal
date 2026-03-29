classDiagram

    class PriorityLevel {
        <<enumeration>>
        LOW = 1
        MEDIUM = 2
        HIGH = 3
    }

    class Owner {
        -name: str
        -pets: List~Pet~
        +add_pet(pet: Pet)
        +to_dict(): dict
        +save_to_json(filepath: str)
        +load_from_json(filepath: str)$
    }

    class Pet {
        -name: str
        -type: str
        -age: int
        -tasks: List~Task~
        +add_task(task: Task)
        +to_dict(): dict
        +from_dict(data: dict)$
    }

    class Task {
        -name: str
        -duration: int
        -priority: PriorityLevel
        -frequency: str
        -due_date: date
        -completed: bool
        +mark_complete()
        +next_due_date(): date
        +__str__(): str
        +to_dict(): dict
        +from_dict(data: dict)$
    }

    class TaskPet {
        <<namedtuple>>
        +task: Task
        +pet: Pet
    }

    class Scheduler {
        -owner: Owner
        +__init__(owner: Owner)
        +_get_all_tasks(): List~Task~
        +_get_task_pets(): Generator~TaskPet~
        +generate_plan(available_time: int): List~Task~
        +sort_tasks_by_priority()
        +sort_tasks_by_time(ascending: bool): List~Task~
        +sort_tasks_by_start_time_str(scheduled_tasks: List, start_key: str): List
        +filter_tasks_by_pet(pet_name: str): List~TaskPet~
        +filter_tasks_by_status(completed: bool): List~TaskPet~
        +filter_tasks(completed: bool, pet_name: str): List~TaskPet~
        +generate_recurring_instances(days_ahead: int): Generator
        +detect_time_conflicts(scheduled_tasks: List): List~dict~
        +check_for_conflicts(scheduled_tasks: List): List~dict~
        +mark_task_complete(pet: Pet, task: Task): bool
    }

    Owner "1" --> "*" Pet : owns
    Pet "1" --> "*" Task : has
    Task --> PriorityLevel : uses
    Scheduler "1" --> "1" Owner : schedules for
    Scheduler ..> TaskPet : yields
    TaskPet --> Task : wraps
    TaskPet --> Pet : wraps

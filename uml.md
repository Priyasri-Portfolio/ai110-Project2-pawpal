classDiagram
    class Owner {
        -name: str
    }
    
    class Pet {
        -name: str
        -type: str
        -age: int
    }
    
    class Task {
        -name: str
        -duration: int
        -priority: int
        +__str__()
    }
    
    class Scheduler {
        -tasks: List~Task~
        +generate_plan(available_time)
        +sort_tasks_by_priority()
    }
    
    Owner "1" --> "*" Pet : owns
    Pet "1" --> "*" Task : has
    Scheduler "1" --> "*" Task : manages
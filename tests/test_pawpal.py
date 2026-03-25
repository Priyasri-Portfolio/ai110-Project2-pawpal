import pytest
from pawpal_system import Task, Pet, Owner, Scheduler

def test_mark_complete_changes_status():
    """Test that calling mark_complete() changes the task's completed status from False to True."""
    # Create a task
    task = Task(name="Test Task", duration=30, priority=2)

    # Initially, the task should not be completed
    assert task.completed == False

    # Call mark_complete()
    task.mark_complete()

    # After calling mark_complete(), the task should be completed
    assert task.completed == True

def test_adding_task_to_pet_increases_task_count():
    """Test that adding a task to a Pet increases that pet's task count."""
    # Create a pet
    pet = Pet(name="Fluffy", type="cat", age=3)

    # Initially, the pet should have no tasks
    assert len(pet.tasks) == 0

    # Create a task
    task = Task(name="Feed Fluffy", duration=10, priority=3)

    # Add the task to the pet
    pet.add_task(task)

    # After adding the task, the pet should have 1 task
    assert len(pet.tasks) == 1

# NEW TESTS FOR ENHANCED SCHEDULER FEATURES - IMPLEMENTED

def test_sort_tasks_by_time_ascending():
    """Test sorting tasks by duration in ascending order. - NEW TEST IMPLEMENTED"""
    owner = Owner("Test Owner")
    pet = Pet("Test Pet", "dog", 2)
    owner.add_pet(pet)
    
    task1 = Task("Short Task", 10, 1)
    task2 = Task("Long Task", 30, 1)
    task3 = Task("Medium Task", 20, 1)
    
    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)
    
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_tasks_by_time(ascending=True)
    
    # Should be sorted: 10, 20, 30
    assert sorted_tasks[0].duration == 10
    assert sorted_tasks[1].duration == 20
    assert sorted_tasks[2].duration == 30

def test_filter_tasks_by_pet():
    """Test filtering tasks by specific pet. - NEW TEST IMPLEMENTED"""
    owner = Owner("Test Owner")
    pet1 = Pet("Fluffy", "cat", 3)
    pet2 = Pet("Buddy", "dog", 5)
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    
    task1 = Task("Feed Cat", 10, 3)
    task2 = Task("Walk Dog", 30, 2)
    
    pet1.add_task(task1)
    pet2.add_task(task2)
    
    scheduler = Scheduler(owner)
    filtered = scheduler.filter_tasks_by_pet("Fluffy")
    
    assert len(filtered) == 1
    assert filtered[0].task.name == "Feed Cat"
    assert filtered[0].pet.name == "Fluffy"

def test_filter_tasks_by_status():
    """Test filtering tasks by completion status. - NEW TEST IMPLEMENTED"""
    owner = Owner("Test Owner")
    pet = Pet("Test Pet", "dog", 2)
    owner.add_pet(pet)
    
    task1 = Task("Incomplete Task", 10, 3)
    task2 = Task("Complete Task", 20, 2)
    task2.mark_complete()
    
    pet.add_task(task1)
    pet.add_task(task2)
    
    scheduler = Scheduler(owner)
    incomplete = scheduler.filter_tasks_by_status(completed=False)
    complete = scheduler.filter_tasks_by_status(completed=True)
    
    assert len(incomplete) == 1
    assert len(complete) == 1
    assert incomplete[0].task.name == "Incomplete Task"
    assert complete[0].task.name == "Complete Task"


def test_filter_tasks_combined_status_and_pet():
    """Test filtering by status + pet name. - NEW TEST IMPLEMENTED"""
    owner = Owner("Test Owner")
    pet1 = Pet("Fluffy", "cat", 3)
    pet2 = Pet("Buddy", "dog", 5)
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    t1 = Task("Feed Fluffy", 10, 3)
    t2 = Task("Walk Buddy", 20, 2)
    t2.mark_complete()

    pet1.add_task(t1)
    pet2.add_task(t2)

    scheduler = Scheduler(owner)
    filtered = scheduler.filter_tasks(completed=True, pet_name="Buddy")

    assert len(filtered) == 1
    assert filtered[0].task.name == "Walk Buddy"
    assert filtered[0].pet.name == "Buddy"


def test_mark_task_complete_recurring_creates_new_instance():
    """Test that completing a daily/weekly task creates the next task instance. - NEW TEST IMPLEMENTED"""
    owner = Owner("Test Owner")
    pet = Pet("Rex", "dog", 4)
    owner.add_pet(pet)

    task = Task("Walk", 30, 2, frequency="daily")
    pet.add_task(task)

    scheduler = Scheduler(owner)
    result = scheduler.mark_task_complete(pet, task)

    assert result is True
    assert task.completed is True
    assert len(pet.tasks) == 2
    assert pet.tasks[1].name == "Walk"
    assert pet.tasks[1].completed is False


def test_detect_time_conflicts():
    """Test basic conflict detection. - NEW TEST IMPLEMENTED"""
    owner = Owner("Test Owner")
    pet = Pet("Test Pet", "dog", 2)
    owner.add_pet(pet)
    
    task1 = Task("Task 1", 10, 3)
    task2 = Task("Task 2", 20, 2)
    
    scheduler = Scheduler(owner)
    
    # Create schedule with overlap: task1 starts at 9:00 (ends 9:10), task2 starts at 9:05
    schedule = [
        {'task': task1, 'pet': pet, 'start_time': 9 * 60},      # 9:00
        {'task': task2, 'pet': pet, 'start_time': 9 * 60 + 5},  # 9:05 (5 min overlap)
    ]
    
    conflicts = scheduler.detect_time_conflicts(schedule)
    
    assert len(conflicts) == 1
    assert conflicts[0]['overlap_minutes'] == 5
    assert conflicts[0]['task1'].name == "Task 1"
    assert conflicts[0]['task2'].name == "Task 2"


def test_sort_tasks_by_start_time_str():
    """Test sorting scheduled tasks by HH:MM string key. - NEW TEST IMPLEMENTED"""
    owner = Owner("Test Owner")
    pet = Pet("Test Pet", "dog", 2)
    owner.add_pet(pet)

    t1 = Task("Morning", 10, 3)
    t2 = Task("Noon", 20, 2)
    t3 = Task("Evening", 15, 1)

    schedule = [
        {'task': t2, 'pet': pet, 'start_time_str': '12:00'},
        {'task': t3, 'pet': pet, 'start_time_str': '18:00'},
        {'task': t1, 'pet': pet, 'start_time_str': '09:00'},
    ]

    scheduler = Scheduler(owner)
    sorted_schedule = scheduler.sort_tasks_by_start_time_str(schedule)

    assert sorted_schedule[0]['task'].name == 'Morning'
    assert sorted_schedule[1]['task'].name == 'Noon'
    assert sorted_schedule[2]['task'].name == 'Evening'

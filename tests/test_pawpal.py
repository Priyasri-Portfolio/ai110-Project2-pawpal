import pytest
from pawpal_system import Task, Pet

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
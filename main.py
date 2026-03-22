from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner
owner = Owner("John Doe")

# Create at least two pets
pet1 = Pet("Fluffy", "cat", 3)
pet2 = Pet("Buddy", "dog", 5)

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create at least three tasks with different times
task1 = Task("Feed", 10, 3)  # 10 min, priority 3
task2 = Task("Walk", 30, 2)  # 30 min, priority 2
task3 = Task("Groom", 20, 1)  # 20 min, priority 1

# Add tasks to pets
pet1.add_task(task1)
pet2.add_task(task2)
pet1.add_task(task3)

# Create scheduler
scheduler = Scheduler(owner)

# Generate plan for available time, say 60 minutes
plan = scheduler.generate_plan(60)

# Print today's schedule
print("Today's schedule:")
for task in plan:
    print(f"- {task}")

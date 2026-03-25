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

print("=== DEMONSTRATING NEW SCHEDULER FEATURES ===\n")  # NEW DEMONSTRATIONS START HERE

# 1. Sorting by time (duration)
print("1. SORTING TASKS BY TIME (shortest first):")
sorted_tasks = scheduler.sort_tasks_by_time(ascending=True)
for task in sorted_tasks:
    print(f"  - {task.name}: {task.duration} min")

print("\n2. SORTING TASKS BY TIME (longest first):")
sorted_tasks = scheduler.sort_tasks_by_time(ascending=False)
for task in sorted_tasks:
    print(f"  - {task.name}: {task.duration} min")

# 2. Filtering by pet
print("\n3. FILTERING TASKS BY PET (Fluffy):")
fluffy_tasks = scheduler.filter_tasks_by_pet("Fluffy")
for tp in fluffy_tasks:
    print(f"  - {tp.task.name} for {tp.pet.name}")

# 3. Filtering by status
print("\n4. FILTERING BY STATUS (incomplete tasks):")
incomplete_tasks = scheduler.filter_tasks_by_status(completed=False)
for tp in incomplete_tasks:
    print(f"  - {tp.task.name} ({tp.task.completed}) for {tp.pet.name}")

# 4. Recurring tasks
print("\n5. GENERATING RECURRING TASK INSTANCES (next 3 days):")
recurring_instances = list(scheduler.generate_recurring_instances(days_ahead=3))
for instance in recurring_instances:
    print(f"  - {instance['task'].name} for {instance['pet'].name} on {instance['date']}")

# 5. Basic conflict detection (simulate a schedule with start times)
#addiong warning insrtead of manual conflict detection to show how it works without needing to implement a full schedule with start times
print("\n6. CONFLICT DETECTION (LIGHTWEIGHT WARNING):")
# Two tasks at overlapping times (same as before)
sample_schedule = [
    {'task': task1, 'pet': pet1, 'start_time': 9 * 60},        # 9:00
    {'task': task2, 'pet': pet2, 'start_time': 9 * 60 + 5},    # 9:05 (overlaps)
    {'task': task3, 'pet': pet1, 'start_time': 10 * 60},       # 10:00
]

warning_msg = scheduler.check_for_conflicts(sample_schedule)
print(warning_msg)

# 8. Add tasks out of order and sort by HH:MM string using new function - NEW DEMONSTRATION IMPLEMENTED
print("\n8. ADD OUT-OF-ORDER TASKS + SORT BY start_time_str:")
out_of_order_schedule = [
    {'task': task2, 'pet': pet2, 'start_time_str': '14:00'},
    {'task': task1, 'pet': pet1, 'start_time_str': '09:30'},
    {'task': task3, 'pet': pet1, 'start_time_str': '13:15'},
]

sorted_by_time_str = scheduler.sort_tasks_by_start_time_str(out_of_order_schedule)
for item in sorted_by_time_str:
    print(f"  - {item['task'].name} at {item['start_time_str']} for {item['pet'].name}")

# 9. Compound filter: completed + pet name - NEW DEMONSTRATION IMPLEMENTED
print("\n9. COMPOUND FILTER: pet=Buddy and completed=True")
# Mark task2 complete to test
task2.mark_complete()
filtered = scheduler.filter_tasks(completed=True, pet_name='Buddy')
for tp in filtered:
    print(f"  - {tp.task.name} (completed={tp.task.completed}) for {tp.pet.name}")

# Original functionality still works
print("\n10. ORIGINAL FUNCTIONALITY - Generate plan for 60 minutes:")
plan = scheduler.generate_plan(60)
print("Today's schedule:")
for task in plan:
    print(f"- {task}")

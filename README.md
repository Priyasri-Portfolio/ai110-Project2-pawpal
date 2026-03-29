# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## PawPal+ Features

### Data Modeling
- **Multi-pet ownership** — An `Owner` holds a list of `Pet` objects; pets can be added dynamically at runtime
- **Task ownership per pet** — Each `Pet` maintains its own task list, so tasks are scoped to the animal they belong to
- **Priority levels via enum** — Task priority is enforced through a `PriorityLevel` enum (LOW=1, MEDIUM=2, HIGH=3), preventing invalid values

### Scheduling
- **Priority-based plan generation** — Uses a min-heap (`heapq`) to efficiently select the highest-priority tasks that fit within an available time budget
- **Sorting by priority** — Tasks across all pets can be ranked highest-to-lowest by `PriorityLevel` value
- **Sorting by duration** — Tasks can be ordered shortest-to-longest or longest-to-shortest, useful for time-boxing a session
- **Sorting by start time string** — A list of scheduled task dicts can be sorted by `HH:MM` string fields using `datetime.strptime` parsing

### Filtering
- **Filter by pet name** — Retrieves only the tasks belonging to a specific pet
- **Filter by completion status** — Separates completed vs. incomplete tasks across all pets
- **Combined filter** — Applies both pet name and completion status filters simultaneously in a single pass

### Recurrence
- **Daily recurrence** — Tasks marked `frequency="daily"` automatically generate instances for every day in a lookahead window
- **Weekly recurrence** — Tasks marked `frequency="weekly"` generate instances every 7 days in the same window
- **Next due date calculation** — `next_due_date()` on a `Task` computes the following occurrence date based on its frequency
- **Auto-scheduling next instance on completion** — When a recurring task is marked complete, a fresh instance for the next due date is automatically added to the pet's task list

### Conflict Detection
- **Overlap detection** — Scans a sorted schedule and flags any pair of tasks where one task's end time exceeds the next task's start time
- **Conflict warning messages** — Returns a human-readable warning listing each overlapping pair and the overlap duration in minutes

### Persistence
- **JSON save** — The full owner-pet-task tree is serialized to `data.json` via `to_dict()` on each class
- **JSON load** — `Owner.load_from_json()` reconstructs the entire object graph from file, including nested pets and tasks
- **Session restore** — The Streamlit app checks for a saved `data.json` on startup and restores the previous owner state automatically

## 📸 Demo
<a href="pawpal_demo.png" target="_blank">
  <img src="pawpal_demo.png"
       title="PawPal App"
       width="600"
       alt="PawPal App Screenshot"
       class="center-block" />
</a>

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

##Testing PawPal+

    -PawPal+ includes an automated test suite to verify the code scheduling logic. these tests ensure that the system behaves correctly as new features are added. 

### Running the test suite
    to run the tests, use:

    '''bash
    python -m pytest

### What the test covers:
    -Sorting correctness:Makes sure tasks are sorted properly by duration and by time straings(HH:MM)
    -Filtering logic:Confirms that tasks can be filtered by pet, completion status, or both.
    -Recurring task behavior-Varifies that completing a daily task automatically creates the next instnace for the following day.
    -Confilt detection:checks that overlapping tasks are identified and reported.
    -Basic tasks and pet operations: ensures that adding tasks and marking them complete works as expected.

    ### Confident Level:⭐⭐⭐⭐☆ (4/5) All  tests pass successfully, and the suite covers the most important scheduling behaviors. The system is reliable for typical use cases, maybe more complex scheduling senarios could be added in the future.

    ## Optional Extentions
    # Challenge 2:Data Preristance with agent Mode: To make PawPal+ to make it more like a real application, I added "data presistance" so that pets and tasks are saved between app sessions.

    ###How it works:
    I extended the core classes in 'pawpal_system.py' with JSON serialization methods:
    -'Task.to_dict()'/ 'Task.from_dict()'
    -'Pet.to_dict()'/ 'Pet.from_dict()'
    -'Owner.to_dict()', 'save_to_json()', and 'load_from_json()'
    These methods convert the in-memory objects into JSON-friendly dictionaries and reconstruct them when the app loads.

    ###Steamlit Integration:
    In app.py, 
    -**loads saved data on startup** using 'Owner.load_from_json()'
    -**saves data automatically** whenever the user adds a pet or task using 'owner.save_to_json()'
    This allows PawPal+ to remember the owner’s pets and tasks even after the app is closed and reopened.

### Why This Matters

    Persistence makes PawPal+ more realistic and user‑friendly.  
    Instead of starting from scratch every time, the app now behaves like a true personal assistant that remembers your pets and their care routines.
        

    #Challenge 3:Advanced priority scheduling and UI :## Optional Extension: Advanced Priority Scheduling & UI Enhancements (Challenge 3)

To make PawPal+ smarter and more user‑friendly, I implemented an enhanced priority system and upgraded the UI to visually communicate task importance.

### Priority-Based Scheduling

Tasks in PawPal+ now support three priority levels:

- **High**
- **Medium**
- **Low**

Each priority level maps to a numeric weight internally, allowing the scheduler to sort tasks by:

1. **Priority first** (High → Medium → Low)
2. **Duration second**

This ensures that the most important tasks always appear at the top of the schedule, even if they take longer or shorter amounts of time.

### UI Enhancements

To make the interface more intuitive, I added:

- **Emoji indicators** for priority  
  - 🔴 High  
  - 🟡 Medium  
  - 🟢 Low  
- **Color-coded labels** in the task table  
- **Cleaner HTML table formatting** for readability

These visual cues help users quickly scan their tasks and understand which ones matter most at a glance.

### Why This Matters

This extension improves both the intelligence and the usability of PawPal+.  
The scheduling logic becomes more aligned with real-world decision-making, and the UI becomes more polished and professional, making the app feel more like a real productivity tool.

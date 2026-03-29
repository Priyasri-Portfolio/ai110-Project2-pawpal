import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler, PriorityLevel

loaded_owner = Owner.load_from_json()

def get_priority_display(priority_str):
    """Return emoji and color for priority level."""
    priority_lower = priority_str.lower()
    if priority_lower == "high":
        return "🔴", "red"
    elif priority_lower == "medium":
        return "🟡", "orange"
    elif priority_lower == "low":
        return "🟢", "green"
    else:
        return "⚪", "gray"

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# Initialize owner in session state if not present
if "owner" not in st.session_state:
    loaded_owner = Owner.load_from_json()
    if loaded_owner:
        st.session_state.owner = loaded_owner
    else:
        st.session_state.owner = Owner(name="Jordan")

owner = st.session_state["owner"]

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# Add pets
if st.button("Add Pet"):
    try:
        new_pet = Pet(name=pet_name, type=species, age=0)  # Age could be added as an input
        owner.add_pet(new_pet)
        owner.save_to_json()
        st.success(f"Added pet: {pet_name}")
    except ValueError as e:
        st.error(f"Error adding pet: {e}")

st.subheader("Your Pets")
for pet in owner.pets:
    st.write(f"- {pet.name} ({pet.type})")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=2)

if st.button("Add task"):
    emoji, color = get_priority_display(priority)
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority,
            "display": f"{emoji} {task_title} ({duration} min) - "
                       f"<span style='color:{color}; font-weight:bold;'>{priority.upper()}</span>"
        }
    )
    owner.save_to_json()

if st.session_state.tasks:
    st.write("Current tasks:")
    table_html = """
    <table style="width:100%; border-collapse: collapse;">
        <thead>
            <tr style="background-color: #f0f0f0;">
                <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Task</th>
                <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Duration</th>
                <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Priority</th>
            </tr>
        </thead>
        <tbody>
    """
    for task in st.session_state.tasks:
        emoji, color = get_priority_display(task["priority"])
        table_html += f"""
            <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">{emoji} {task["title"]}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">{task["duration_minutes"]} min</td>
                <td style="border: 1px solid #ddd; padding: 8px; color:{color}; font-weight:bold;">{task["priority"]}</td>
            </tr>
        """
    table_html += "</tbody></table>"
    st.markdown(table_html, unsafe_allow_html=True)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):

    # Map UI priority strings to PriorityLevel enum
    priority_map = {
        "High": PriorityLevel.HIGH,
        "Medium": PriorityLevel.MEDIUM,
        "Low": PriorityLevel.LOW
    }

    # Convert session tasks into Task objects
    task_objects = [
        Task(
            name=t["title"],
            duration=t["duration_minutes"],
            priority=priority_map[t["priority"]]
        )
        for t in st.session_state.tasks
    ]

    # Create scheduler
    scheduler = Scheduler(owner)

    # Attach UI-created tasks to the scheduler
    scheduler.tasks = task_objects

    # 1. Sort tasks (in place)
    scheduler.sort_tasks_by_priority()
    sorted_tasks = scheduler.tasks

    st.subheader("📋 Sorted Tasks (by Priority)")
    st.table([
        {
            "Task": t.name,
            "Duration": f"{t.duration} min",
            "Priority": t.priority.name
        }
        for t in sorted_tasks
    ])

    # 2. Generate schedule (example: 3 hours available)
    plan = scheduler.generate_plan(available_time=180)

    st.subheader("🗓️ Generated Schedule")
    if plan:
        st.table([
            {
                "Task": t.name,
                "Duration": f"{t.duration} min"
            }
            for t in plan
        ])
    else:
        st.info("No tasks fit into the available time.")

    # 3. Conflict warnings (placeholder: you’d pass real scheduled_tasks later)
    conflicts = scheduler.detect_time_conflicts([])

    if conflicts:
        st.warning("⚠️ Some tasks in your schedule conflict.")
        with st.expander("View conflict details"):
            for conflict in conflicts:
                st.markdown(
                    f"""
                    **Conflict detected:**  
                    - 🐾 **{conflict['task1'].name}**  
                    - 🐾 **{conflict['task2'].name}**  
                    **Overlap:** {conflict['overlap_minutes']} minutes
                    """
                )
    else:
        st.success("🎉 No conflicts detected!")

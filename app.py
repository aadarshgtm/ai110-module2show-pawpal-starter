import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# Initialize session state for Owner
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Default Owner")

owner = st.session_state.owner

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
owner_name = st.text_input("Owner name", value=owner.name)
if owner_name != owner.name:
    owner.name = owner_name
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    new_pet = Pet(name=pet_name, species=species)
    owner.add_pet(new_pet)
    st.success(f"Added pet {pet_name}!")

st.markdown("### Current Pets")
if owner.pets:
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets added yet.")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if owner.pets:
    pet_options = [pet.name for pet in owner.pets]
    selected_pet = st.selectbox("Select Pet for Task", pet_options)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    with col4:
        time = st.text_input("Time (HH:MM)", value="08:00")

    if st.button("Add task"):
        selected_pet_obj = next(pet for pet in owner.pets if pet.name == selected_pet)
        new_task = Task(description=task_title, time=time, frequency="daily", priority=priority, duration_minutes=duration)
        selected_pet_obj.add_task(new_task)
        st.success(f"Added task '{task_title}' to {selected_pet}!")
else:
    st.warning("Add a pet first before adding tasks.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    if owner.pets and any(pet.tasks for pet in owner.pets):
        scheduler = Scheduler(owner)
        schedule = scheduler.get_schedule()
        conflicts = scheduler.detect_conflicts(schedule)
        
        st.markdown("### Today's Schedule")
        schedule_data = []
        for task in schedule:
            status = "✓" if task.completed else "○"
            schedule_data.append({
                "Time": task.time,
                "Task": task.description,
                "Pet": task.pet_name,
                "Priority": task.priority,
                "Status": "Completed" if task.completed else "Pending"
            })
        st.table(schedule_data)
        
        if conflicts:
            st.warning("Conflicts detected:")
            for conflict in conflicts:
                st.write(conflict)
        else:
            st.success("No conflicts detected!")
    else:
        st.warning("Add pets and tasks first.")

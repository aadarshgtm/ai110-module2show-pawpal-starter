from pawpal_system import Owner, Pet, Task, Scheduler

# Create an Owner
owner = Owner(name="Jordan")

# Create Pets
pet1 = Pet(name="Mochi", species="dog")
pet2 = Pet(name="Whiskers", species="cat")

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create Tasks
task1 = Task(description="Morning walk", time="08:00", frequency="daily", priority="high")
task2 = Task(description="Feed breakfast", time="07:00", frequency="daily", priority="medium")
task3 = Task(description="Evening play", time="18:00", frequency="daily", priority="low")
task4 = Task(description="Vet appointment", time="10:00", frequency="once", priority="high")

# Add tasks to pets
pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)
pet1.add_task(task4)

# Create Scheduler
scheduler = Scheduler(owner)

# Get and print schedule
schedule = scheduler.get_schedule()
print("Today's Schedule:")
for task in schedule:
    status = "✓" if task.completed else "○"
    print(f"{status} {task.time} - {task.description} ({task.pet_name}) - Priority: {task.priority}")

# Test filtering
print("\nFiltered tasks for Mochi:")
mochi_tasks = scheduler.filter_tasks(schedule, pet_name="Mochi")
for task in mochi_tasks:
    print(f"{task.time} - {task.description}")

# Test recurring
print("\nTesting recurring task:")
recurring_task = Task(description="Daily feed", time="07:00", frequency="daily", priority="high")
pet1.add_task(recurring_task)
print(f"Tasks before marking complete: {len(pet1.get_tasks())}")
pet1.mark_task_complete(recurring_task)
print(f"Tasks after marking complete: {len(pet1.get_tasks())}")
print("New task added:", pet1.get_tasks()[-1].description if len(pet1.get_tasks()) > 4 else "None")

# Test persistence
print("\nTesting data persistence:")
owner.save_to_json("test_data.json")
loaded_owner = Owner.load_from_json("test_data.json")
print(f"Original owner: {owner.name}, {len(owner.pets)} pets")
print(f"Loaded owner: {loaded_owner.name}, {len(loaded_owner.pets)} pets")
print("Persistence test passed!")
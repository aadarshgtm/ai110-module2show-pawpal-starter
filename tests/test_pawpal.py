import pytest
from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    task = Task(description="Test task", time="12:00", frequency="once", priority="medium")
    assert not task.completed
    task.mark_complete()
    assert task.completed

def test_task_addition():
    pet = Pet(name="TestPet", species="dog")
    task = Task(description="Test task", time="12:00", frequency="once", priority="medium")
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1
    assert pet.get_tasks()[0].description == "Test task"

def test_scheduler_sorting():
    owner = Owner(name="TestOwner")
    pet = Pet(name="TestPet", species="dog")
    owner.add_pet(pet)
    
    task1 = Task(description="Task 1", time="10:00", frequency="once", priority="medium")
    task2 = Task(description="Task 2", time="08:00", frequency="once", priority="medium")
    pet.add_task(task1)
    pet.add_task(task2)
    
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time([task1, task2])
    assert sorted_tasks[0].time == "08:00"
    assert sorted_tasks[1].time == "10:00"

def test_scheduler_filtering():
    owner = Owner(name="TestOwner")
    pet1 = Pet(name="Pet1", species="dog")
    pet2 = Pet(name="Pet2", species="cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    
    task1 = Task(description="Task1", time="12:00", frequency="once", priority="medium")
    task2 = Task(description="Task2", time="12:00", frequency="once", priority="medium")
    pet1.add_task(task1)
    pet2.add_task(task2)
    
    scheduler = Scheduler(owner)
    filtered = scheduler.filter_tasks([task1, task2], pet_name="Pet1")
    assert len(filtered) == 1
    assert filtered[0].pet_name == "Pet1"

def test_conflict_detection():
    owner = Owner(name="TestOwner")
    pet = Pet(name="TestPet", species="dog")
    owner.add_pet(pet)
    
    task1 = Task(description="Task1", time="12:00", frequency="once", priority="medium")
    task2 = Task(description="Task2", time="12:00", frequency="once", priority="medium")
    pet.add_task(task1)
    pet.add_task(task2)
    
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts([task1, task2])
    assert len(conflicts) == 1
    assert "Conflict at 12:00" in conflicts[0]
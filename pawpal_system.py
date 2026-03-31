from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional


@dataclass
class Task:
    """Represents a single pet care activity."""
    description: str
    time: str                          # "HH:MM" format
    frequency: str                     # "once", "daily", "weekly"
    priority: str                      # "low", "medium", "high"
    duration_minutes: int = 30
    completed: bool = False
    due_date: Optional[date] = None
    pet_name: str = ""  # Add this to associate task with pet

    def mark_complete(self):
        self.completed = True

    def is_recurring(self) -> bool:
        return self.frequency != "once"


@dataclass
class Pet:
    """Represents a pet owned by an Owner."""
    name: str
    species: str                       # "dog", "cat", "other"
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        task.pet_name = self.name
        self.tasks.append(task)

    def get_tasks(self) -> list:
        return self.tasks

    def mark_task_complete(self, task: Task):
        task.mark_complete()
        if task.is_recurring():
            # Create new task for next occurrence
            new_due_date = task.due_date or date.today()
            if task.frequency == "daily":
                new_due_date += timedelta(days=1)
            elif task.frequency == "weekly":
                new_due_date += timedelta(weeks=1)
            new_task = Task(
                description=task.description,
                time=task.time,
                frequency=task.frequency,
                priority=task.priority,
                duration_minutes=task.duration_minutes,
                completed=False,
                due_date=new_due_date
            )
            self.add_task(new_task)


@dataclass
class Owner:
    """Represents the pet owner who manages one or more pets."""
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self) -> list:
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """The brain of PawPal+. Retrieves, sorts, filters, and manages tasks."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_schedule(self) -> list:
        tasks = self.owner.get_all_tasks()
        return self.sort_by_time(tasks)

    def sort_by_time(self, tasks: list) -> list:
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return sorted(tasks, key=lambda t: (priority_order[t.priority], t.time))

    def filter_tasks(self, tasks: list, pet_name: str = None, completed: bool = None) -> list:
        filtered = tasks
        if pet_name:
            filtered = [t for t in filtered if t.pet_name == pet_name]
        if completed is not None:
            filtered = [t for t in filtered if t.completed == completed]
        return filtered

    def detect_conflicts(self, tasks: list) -> list:
        conflicts = []
        time_dict = {}
        for task in tasks:
            if task.time in time_dict:
                conflicts.append(f"Conflict at {task.time}: {time_dict[task.time].description} and {task.description}")
            else:
                time_dict[task.time] = task
        return conflicts

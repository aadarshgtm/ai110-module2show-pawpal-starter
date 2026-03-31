from dataclasses import dataclass, field
from datetime import date
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

    def mark_complete(self):
        pass

    def is_recurring(self) -> bool:
        pass


@dataclass
class Pet:
    """Represents a pet owned by an Owner."""
    name: str
    species: str                       # "dog", "cat", "other"
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self) -> list:
        pass


@dataclass
class Owner:
    """Represents the pet owner who manages one or more pets."""
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self) -> list:
        pass


class Scheduler:
    """The brain of PawPal+. Retrieves, sorts, filters, and manages tasks."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_schedule(self) -> list:
        pass

    def sort_by_time(self, tasks: list) -> list:
        pass

    def filter_tasks(self, tasks: list, pet_name: str = None, completed: bool = None) -> list:
        pass

    def detect_conflicts(self, tasks: list) -> list:
        pass

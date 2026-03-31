## 1. System Design

**a. Initial design**

Three core user actions the app supports:

1. Add a pet (name, species) to the owner's profile
2. Add a care task (walk, feeding, medication, etc.) to a specific pet with a time and priority
3. Generate a daily schedule that sorts and displays all tasks in chronological order, prioritizing by priority then time

The system is built around four classes:

- **Task** — holds a single activity's details (description, time, frequency, priority, duration, completion status). Responsible for tracking whether a task is done and whether it recurs.
- **Pet** — stores a pet's name and species, and maintains a list of that pet's tasks. Responsible for adding and retrieving tasks, and handling recurring task creation.
- **Owner** — holds the owner's name and a list of their pets. Responsible for aggregating tasks across all pets.
- **Scheduler** — the "brain" of the app. Takes an Owner and provides methods to retrieve, sort, filter, and detect conflicts in the full task list.

**b. Design changes**

Added pet_name to Task for easier filtering. Added mark_task_complete in Pet to handle recurring tasks by creating new instances.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers time (for sorting), priority (high > medium > low), and pet association (for filtering). It prioritizes high-priority tasks first, then sorts by time.

**b. Tradeoffs**

Only checks for exact time matches for conflicts, not overlapping durations, to keep it simple.

---

## 3. AI Collaboration

**a. How you used AI**

Used AI to generate class skeletons, implement methods, create tests, and integrate UI.

**b. Judgment and verification**

Accepted most suggestions but verified with tests.

---

## 4. Testing and Verification

**a. What you tested**

Task completion, addition, sorting, filtering, conflicts.

**b. Confidence**

High, all tests pass.

---

## 5. Reflection

**a. What went well**

Implementing OOP and connecting to UI.

**b. What you would improve**

Add more advanced conflict detection.

**c. Key takeaway**

AI helps speed up development but human oversight is key.

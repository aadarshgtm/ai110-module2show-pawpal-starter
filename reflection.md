# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

Three core user actions the app supports:
1. Add a pet (name, species) to the owner's profile
2. Add a care task (walk, feeding, medication, etc.) to a specific pet with a time and priority
3. Generate a daily schedule that sorts and displays all tasks in chronological order

The system is built around four classes:
- **Task** — holds a single activity's details (description, time, frequency, priority, duration, completion status). Responsible for tracking whether a task is done and whether it recurs.
- **Pet** — stores a pet's name and species, and maintains a list of that pet's tasks. Responsible for adding and retrieving tasks.
- **Owner** — holds the owner's name and a list of their pets. Responsible for aggregating tasks across all pets.
- **Scheduler** — the "brain" of the app. Takes an Owner and provides methods to retrieve, sort, filter, and detect conflicts in the full task list.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
    -Initial UML design includes four main classes. 
- What classes did you include, and what responsibilities did you assign to each?
    -I have included these classes: Owner,Pet,Task,and Scheduler. 
    -The Owner class stored basic information about the pet owner.
    -The Pet class stored details about the pet, such as name and type.
    -The task class represented a single pet-care activity and included attriibutes like name, duration, and priority.
    -The Scheduler class was responsible for selecting tasks based on constrains such as available time and priority.

**1)b). Design Changes**
    After asking the copilot to review the skeleton of the file:pawpal_system.py missing relationships or potential bottlenecks, copilot suggested few changes. It suggests for several improvements that made the design more complete and it also matches the UML. 1)It added the list of pets to the Owner. One owner may have more than one pet. 2)Now the pets has a list of tasks. 3)Now the pets has a condition for the age, it can't be negative,makes sense. 4)Tasls now validates duration and priority. 5)Scheduler now takes an Owner instead of list of tasks, so that it starts from the Owner->Pets->Tasks. This matched the UML diagram and the logic.6) Now the Scheduler has a helper method, cleaner code. Overall these improments are little more details and matched the UML flow.
    ---

    

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
    -My scheduler considers several key constraints
    *Task duration, task priority, task frequency, start times,and pet association.
- How did you decide which constraints mattered most?
    I decided that task priorities and the task duration mattered most, because these tasks directly affect the schedule. It will be like a deciding factor. Priority ensures that essiential tasks are taken care, like feeding rather than choosing grooming, it can me skipped. Frequncy and conflict detection and intellegent, but they come after the core scheduling logic. 
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
    -One tradeoff my schedule makes is using a simple, adjacent-comparison detection algorithm. After sorting tasks by start time, it only checks each task against the next one in the list. 
- Why is that tradeoff reasonable for this scenario?
    -This keeps the method lightweight, readable, and efficient, but it means the scheduler does not detect every possible ovelapping pair, only neighbors.It keeps the algorithm easy to understand and maintain. It avoids unneccessary complexity, like nested loops or intervals. It aligns with the project's goal of building clear, beginner-friendly scheduling logic rathar than a full schedular.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
    I used AI for understanding the code, logic or used AI more like a tutor. Understand something that's I am not familiar, why I am adding something and Ai is suggesting to change the code, more clearity.
- What kinds of prompts or questions were most helpful?
    Specific propmt with help me understand the piece of code. Explain the class and the methods. Modifying certain elements in the code, how would that impact the function or make it better. Help me implement, or documention. The Codepath project instuctions helped me to prompt properly. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
    I think on the edge cases it was giving some complecated suggestions, i really didn't understand. I thought those not necessary to make the changes. For Example, AI suggested to a plan class and related algorithm. It's not a bad suggession, but this this project the scenarios, we don't need to make it compleccated. 
-Did you evaluate or verify what the AI suggested?
    Yes, I verified, evaluated, and tested the suggestions. It let me in to a tangle. It took me a great time to untangle the mess. Especially at the phase 6, steps 1-3. But it was a great leanring. 

---

## 4. Testing and Verification

**a. What you tested**
    -I tested the core behavior of the scheduler, including sorting tasks, filtering by pet or completion status, generating recurring tasks, detecting the overlaps. These tests helped ensure that the logic stayed consistent even as added new features nad refined the class structure. These are important for validating priority handling and recurrence. Overall, the tests gave me confidence that the system behaves predictably across typical use cases.
- What behaviors did you test?
    -Tested the core behaviors of the scheduler:sorting tasks, filtering by pets or completion status, generating recurring taks, and detecting overlaps. These tests helped me verify that the logic worked consistantly even as I added new features. I feel confident in the scheduler's correctness for typical use cases, especialy around priority handling and recurrence.
- Why were these tests important?
    These tests are important because, it evaluated the model and the algorithm's nested structure. It helped me check the edge cases nad different scenarios. By testing each behavior separately, I could isolate issues quickly and maintain a clean, reliable design.
**b. Confidence**

- How confident are you that your scheduler works correctly?
    -I am cofident that the scheduler work well. I am satisfied with how clean ands organized my final system design turned out. Especially the way the Owner->Pet->Task strucute flows naturally and makes sense.
- What edge cases would you test next if you had more time?
    -If I had more time I would explore more complex edge cases and more advanced algorithm. This project helped me understand that designing systems requires balancing clarity with functionality, and working with AI responsibily.
---

## 5. Reflection

**a. What went well**
    -The project instructions gave me a clear structure to follow, which made it easier to build the system step by step. I felt supported by the flow of the assignment, and it helped me stay organized as the project grew. Overall, the guided steps made the whole process feel manageable instead of overwhelming. 
- What part of this project are you most satisfied with?
    -I’m most satisfied with how clean and organized my final system design turned out. The way the classes connect—Owner → Pet → Task—made the scheduling logic intuitive and easy to extend. I also liked how the UI and backend eventually aligned smoothly after debugging the mismatches.
    
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
    -If I had another iteration, I would improve the UI‑to‑backend integration and make the schedule display more dynamic and informative. I’d also explore a more advanced scheduling algorithm that considers more constraints without sacrificing clarity. Strengthening the conflict‑detection logic would be another area worth refining.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
    The biggest thing I learned is that working with AI still requires strong human judgment. AI can speed up brainstorming, debugging, and refactoring, but it’s up to me to guide the architecture and keep the design clean. This project taught me how to collaborate with AI intentionally while staying in control of the final decisions.

Seating

Jessica Novillo Argudo

CSCI 77800 Fall 2022
___

Directions:

- Design an algorithm that would seat people more equitably.

- Write up a description of your algorithm and save it as week09_seating/seating.pdf (or week09_seating/seating.md). Make sure this description states how it should improve equity and also how it might affect other concerns.

- NO CODE IS NEEDED OR EXPECTED HERE -- just a description -- but make a note of implementation issues that might make your algorithm more practical or more difficult to implement

- In class next week you will share your ideas and algorithms and ultimately decide on what to recommend to the airlines.

___

### Algorithm Description

My algorithm would have the following considerations. These considerations are listed in order of priority:

- People with disabilities: They would choose their seats, and if they travel with a companion, they would also have the option to choose the companion's seat. The algorithm should lock the exit seats so they cannot be selected. 

- Families that include children 0-5 years old: They would choose their seats. The algorithm should validate that at least one adult seats next to the child and that seats are not close to an exit.

- Families that include children 6+ years old: Seats can be randomly assigned, ensuring that at least one adult seats next to the child.

### How should it improve equity?

People with disability, infants, or small children (under 6) need extra support on a plane, which is why I think it is fair to allow them to choose their seats. Older children (6+) do not need the support as small children, but they still need to be supervised by an adult, so it is fair to randomly assign seats but keep at least one adult sitting next to a child. 

### How might it affect other concerns?

Customers like frequent flyers would be dissatisfied if the preferable seats are unavailable because they have been previously assigned to people with special needs or small children.

### Implementation issues that might make your algorithm more difficult to implement

- Validation of age when children are traveling.
- Validation of documents that serve as proof of disability.

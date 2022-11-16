Plane Seating Algorithm

Collaborators: Jessica Novillo Argudo, Harrison Fung, Shana Elizabeth Henry

CSCI 77800 Fall 2022
___

### Rules for economy and economy plus
Families that include at least one child under the age of 12 (for most airlines, a person under 12 is considered a child) will be seated together in the same row if possible. If there is no room to allocate all the family members together in the same row, then each child should be seated next to at least one adult. If there is no room to do that, then the family will be informed that there is no space to allocate them. To reduce complexity, we are considering only one child per family.

Adult groups will be seated together if possible. If there is no room to allocate all the group members together in the same row, they will get separated seats.

People who fly alone will be randomly assigned seats following the current economy and economy plus rules.

### Priority considered for economy seat assignation 
* Family with children
* Adult group
* Flying alone

### Future improvements
Other improvements that could be done but are not implemented for this assignment for time reasons are:

- Include more than one child per family.
- Change the seat configuration to have aisles seats.
- Add priority to people with disabilities.
- People with a disability and their companion should be seated together.

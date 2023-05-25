/*
    Name: Simple Fun #288: Turns On Road
    Rank: 6 kyu
    Prompt: There's a wolf who lives in the plane forest, which is located on the Cartesian coordinate system. When going on the hunt, the wolf starts at point (0, 0) and goes spirally as shown in the picture below:
The wolf finally found something to eat at point (x, y). Your task is to calculate the number of turns he had to make to get to that point.

Input/Output
[input] integer x

x coordinate of the final point.

-1000000 ≤ x ≤ 1000000

[input] integer y

y coordinate of the final point.

-1000000 ≤ y ≤ 1000000

[output] an integer

The number of turns.

Example
For x = 1 and y = 1, the output should be 1.

Path:(0,0) --> (1,0) --> (1,1), 1 turn at (1,0)

For x = 1 and y = -1, the output should be 4.

Path:(0,0) --> (1,0) --> (1,1) --> (-1,1) --> (-1,-1) --> (1,-1),

4 turns at (1,0), (1,1), (-1,1), (-1,-1)
*/

//Solution
function turnsOnRoad(x, y) {
    //coding and coding..
    
    let turns = 0;
    
    if (x > y) {
      if (x + y <= 1) {
        turns = y * -4;
      } else {
        turns = (x - 1) * 4 + 1;
      }
    } else if (x < y) {
      if (x + y < 0) {
        turns = (Math.abs(x) - 1) * 4 + 3;
      } else {
        turns = (Math.abs(y) - 1) * 4 + 2;
      }
    } else {
      if (x > 0) {
        turns = (x - 1) * 4 + 1;
      } else if (x < 0) {
        turns = (Math.abs(x) - 1) * 4 + 3;
      }
    }
    
    console.log(turns);
    return turns;
  }
  /*
  (0,0): x+y = 0
  (0,0) - (1,0): 0 turns (x > y) x+y = 1
  (1,0) - (1,1): 1 turn (y <= x) x+y =2
  (1,1) - (0,1) - (-1,1): 2 turns (y > x)
  (-1,1) - (-1,0) - (-1,-1): 3 turns ()
  (-1,-1) - (0,-1) - (1,-1) - (2, -1): 4 turns
  (2,-1) - (2,0) - (2,1) - (2,2): 5 turns
  (2,2) - (1,2) - (0,2) - (-1,2) - (-2,2): 6 turns
  (1,1) 1
  (-1,1) 2
  (-1,-1) 3
  (2,-1) 4
  ()
  
  What is different between (2, -2) and (3, -1)?
  2 > -2, 3 > -1
  2 + -2 = 0, 3 + -1 = 2
  So turn happens when x + y > 1?
  if x + y = 0 and x < 0: turns = (|x| - 1) * 4 + 2
    if x + y = 0 and x >= 0: turns = 
  */
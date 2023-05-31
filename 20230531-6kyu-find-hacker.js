/*
    Name: Find Cracker.
    Rank: 6 kyu
    Prompt: Someone was hacking the score. Each student's record is given as an array.
     The objects in the array are given again as an array of scores for each name and total score.
     The scores for each grade is:

A: 30 points
B: 20 points
C: 10 points
D: 5 points
Everything else: 0 points
If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded. After all the calculations, the total score should be capped at 200 points.

Returns the name of the hacked name as an array when scoring with this rule.
*/

// Solution:
function findHack(arr) {
    let hackedStudents =  [];
    for (const student of arr) {
      if (student[1] > 200) {
        hackedStudents.push(student[0]);
        console.log(student[0], student[1]);
        continue;
      }
      let gradesScore = 0;
      let bonus = true;
      if (student[2].length < 5) {
        bonus = false;
      }
      for (const grade of student[2]) {
        switch (grade) {
            case "A": 
              gradesScore += 30;
              break;
            case "B":
              gradesScore += 20;
              break;
            case "C":
              gradesScore += 10;
              bonus = false;
              break;
            case "D":
              gradesScore += 5;
              bonus = false;
              break;
            default:
              bonus = false;
        }
      }
      if (bonus) {
        gradesScore += 20;
      }
      console.log(student[0], student[1], gradesScore)
      if (student[1] !== gradesScore) {
        hackedStudents.push(student[0]);
      }
    }
    console.log("Hacked grades: ",hackedStudents);
    return hackedStudents;
  }
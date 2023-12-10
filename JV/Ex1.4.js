'use strict';
const studentName = prompt(' What is your name: ');
let printName = `Welcome, ${studentName} belong to class `;
const randomNo = Math.floor(Math.random() * 4) + 1;
switch(randomNo){
  case 1:
    printName += 'Gryfinndor';
    break;
  case 2:
    printName += 'Slytherin';
    break;
  case 3:
    printName += 'Ravenclaw';
    break;
  case 4:
    printName += 'Hufflepuff';
    break;
}
document.querySelector('#target').innerHTML = printName;
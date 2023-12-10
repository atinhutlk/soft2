'use strict';
/*
console.log("this is a connected")
// commenting out aline in JS
//alert("Helo, How are u?")

const name = "Happy";
console.log(typeof name);
let name1, phoneNum;
name1 = "Happy2";
phoneNum = 4567890;
console.log(name1);
console.log(phoneNum);
const age =19;
const ageStr = age.toString();
console.log(ageStr);
const income = "5765.23";
const incomeNum = parseFloat(income);
console.log(incomeNum)

let allCombined;
allCombined = name1+ ageStr + income;
console.log(allCombined)

//asking the input from the user:
const name2= prompt("What is your name");
console.log("Nice to meet you, " + name2)

let number= 5;
number = number * 2;
number = number/2 +1;


const  ageUser = prompt("How old are you? ");
if(ageUser < 18){
  alert(" You are not eligible to access");
}

const num1 = prompt(" Give me 1st number")
const num2 = prompt("Give me the 2nd number")
if(num1 == num2) {
  console.log(' There are the same values')
}
*/
let num1 = parseInt(prompt('First Number : '));
let num2 = parseInt(prompt('Second number: '));
let helpNum;
helpNum = num1;
num1 = num2;
num2 = helpNum;
doccument.write(' The Value of number now is : ', num1 ,num2)

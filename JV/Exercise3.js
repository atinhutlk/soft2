'use strict';
const firstNo = parseInt(prompt('Enter the 1st number: '))
const secondNo = parseInt(prompt('Enter the 2nd number: '))
const thirdNo = parseInt(prompt('Enter the 3rd number: '))

document.querySelector('#sum').innerHTML = `The sum of 3 numbers : ${firstNo+secondNo+thirdNo}`
document.querySelector('#product').innerHTML = `The product of 3 numbers : ${firstNo*secondNo*thirdNo}`
document.querySelector('#average').innerHTML = `The average of 3 numbers : ${(firstNo+secondNo+thirdNo)/3}`
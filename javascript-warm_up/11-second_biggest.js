#!/usr/bin/node
const { argv } = require('node:process');
const numbers = argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  let biggest = -Infinity;
  let secondBiggest = -Infinity;

  for (const number of numbers) {
    if (number > biggest) {
      secondBiggest = biggest;
      biggest = number;
    } else if (number > secondBiggest && number < biggest) {
      secondBiggest = number;
    }
  }

  console.log(secondBiggest === -Infinity ? 0 : secondBiggest);
}

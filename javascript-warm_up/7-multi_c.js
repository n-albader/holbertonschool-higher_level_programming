#!/usr/bin/node
const { argv } = require('node:process');
const occurrences = parseInt(argv[2]);

if (Number.isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
}

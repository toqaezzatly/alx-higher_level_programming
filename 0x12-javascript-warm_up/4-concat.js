#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(`${arg1 ? arg1 : 'undefined'} is ${arg2 ? arg2 : 'undefined'}`);


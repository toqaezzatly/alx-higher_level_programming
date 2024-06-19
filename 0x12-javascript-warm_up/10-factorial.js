#!/usr/bin/node

function factorial(n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  }
  
  // Handle NaN case: factorial of NaN is 1
  if (isNaN(n)) {
    return 1;
  }

  // Recursive case: n * factorial(n-1)
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));


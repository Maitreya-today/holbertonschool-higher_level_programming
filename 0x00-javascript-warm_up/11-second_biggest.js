#!/usr/bin/node
function secondLargest (args) {
  if (args.length <= 2) {
    return 0;
  }
  const nums = args.map(Number);
  const largest = Math.max.apply(null, nums);
  const index = nums.indexOf(largest);
  nums.splice(index, 1);
  const secondLargest = Math.max.apply(null, nums);
  return secondLargest;
}

const args = process.argv.slice(2);
console.log(secondLargest(args));

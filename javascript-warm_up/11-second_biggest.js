#!/usr/bin/node
const args = process.argv.slice(2).map(Number); // Convert all arguments to integers

if (args.length <= 1) {
	  console.log(0); // Print 0 if no arguments or only one argument
} else {
	  const secondBiggest = args.sort((a, b) => b - a)[1];
	  console.log(secondBiggest);
}

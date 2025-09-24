#!/usr/bin/node
function add (a, b) {
	  return (a + b);
}
const argv = process.argv.slice(2);
const y = parseInt(argv[0]);
const z = parseInt(argv[1]);

console.log(add(y, z));

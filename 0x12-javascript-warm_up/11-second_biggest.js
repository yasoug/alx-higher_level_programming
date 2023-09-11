#!/usr/bin/node
if (process.argv.length === 2 || process.argv[3] === undefined) {
  console.log('0');
}
if (process.argv.length > 3) {
  const sortedargs = process.argv.slice(2).sort();
  console.log(sortedargs[process.argv.length - 4]);
}

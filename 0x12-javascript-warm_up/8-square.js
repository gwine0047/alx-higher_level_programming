#!/usr/bin/node
const num = process.argv[2];

if (!parseInt(num))
{
  console.log('Missing size');
}
else
{
  for (let i = 0; i < num; i++) {
    let y = 0;
    let myVar = '';

    while (y < num) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}

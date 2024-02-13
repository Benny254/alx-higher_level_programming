#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const map1 = list.map((x, i) => { return x * (i + 1); }); // Adjusted to multiply by (i + 1)
console.log(map1);

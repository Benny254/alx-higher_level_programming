#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let w = 0; w < this.height; w++) console.log(c.repeat(this.width));
    }
  }
};

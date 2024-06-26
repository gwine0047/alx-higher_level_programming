#!/usr/bin/node
/**
 * A Rectangle class being inherited by a class Square
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle
{
  constructor (size)
  {
    super(size, size);
  }
}

module.exports = Square;

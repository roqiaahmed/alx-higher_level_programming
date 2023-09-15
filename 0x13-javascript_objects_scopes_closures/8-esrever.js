#!/usr/bin/node

exports.esrever = function (list) {
  var ret = new Array();
  for (var i = list.length - 1; i >= 0; i--) {
    ret.push(list[i]);
  }
  return ret;
};

#!/usr/bin/env python

def func():
  a, *b, c = ["Tony", "Phony", "Pony"]
  return "Phony" in [b] or a[:]

print(func())

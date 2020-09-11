#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here

  for i in range(n):
    print(['rock', 'rock'], ['rock', 'paper'],['rock', 'scissors'], ['paper', 'scissors'],['paper', 'paper'], ['scisors', 'scisors'])


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
#!/usr/bin/env python
# coding=utf-8

"""
Simple command-line argument parser
"""

import argparse
import sys

def parse_args():
  """Define and handle command-line args, computing defaults as needed."""
  parser = argparse.ArgumentParser(
      formatter_class=argparse.RawTextHelpFormatter, # disable line wrapping, and assume help strings are already formatted
    description="Describe what your program does.")
  parser.add_argument("--arg1",
                      help="Default configuration (not required, string, default: '')")
  parser.add_argument("--arg2",
                      type = int,
                      default = 8000,
                      help = "Parsed as integer, with default"),
  parser.add_argument("--arg3",
                      default = False,
                      action = 'store_true',
                      help = "Boolean, set to true if present")
  parser.add_argument("--arg4",
                      choices=['rock', 'paper', 'scissors'],
                      required = True,
                      help = "Required string with specific allowed values")

  args = parser.parse_args() # returns argparse.Namespace object
  return vars(args)          # convert to more convenient dict representation



args = parse_args() # call argument parser
print(args)

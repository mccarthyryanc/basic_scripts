#!/usr/bin/env python
#
# Quick script to convert a CSV to a TSV
#
# How to use:
#   Provide filename as first argument. TSV formatted is sent to stdout.
#
import sys, csv

f = open(sys.argv[1], 'rU')
try:
    reader = csv.reader(f)
    for row in reader:
        newrow = [str(item) for item in row]
        print "\t".join(newrow)
finally:
    f.close()

#! /usr/bin/env python
#
# Collection of math-related scripts to call from command line.
#
import sys, re, random

class Maths:
    # Method to random floats in range
    @staticmethod
    def rand_range():
        if len(sys.argv) < 2 :
            print "Need more input"
            exit()
        elif len(sys.argv) == 2 :
            num = 10
            x_min = 0.0
            x_max = 0.1
        elif len(sys.argv) == 3 :
            num = float(sys.argv[2])
            x_min = 0.0
            x_max = 0.1
        elif len(sys.argv) == 5 :
            num = float(sys.argv[2])
            x_min = float(sys.argv[3])
            x_max =float(sys.argv[4])
        elif len(sys.argv) > 5 :
            print "TMI, too much input."
            
        curr = 1.0
        while curr <= num:
            print random.uniform(x_min,x_max)
            curr += 1.0

def main():
    if len(sys.argv) >= 2:
        method = sys.argv[1]
    else :
        print "Need more input"
        exit()
    
    if method == 'random':
        Maths.rand_range()
    else:
        print "Provide valid method"
        exit()

if __name__ == "__main__":
    main()

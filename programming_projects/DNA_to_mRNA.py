#!/usr/bin/python3

"""A simple python script template.
"""

import os
import sys
import argparse


def main(arguments):
    tRNA = ""
    if len(arguments):
        for x in arguments[0]:
            if x == "A":
                tRNA += "U"
            elif x == "T":
                tRNA += "A"
            elif x == "G":
                tRNA += "C"
            elif x == "C":
                tRNA += "G"
            else:
                sys.exit("contains invalid nucleotide")
        print(tRNA)
            
        

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
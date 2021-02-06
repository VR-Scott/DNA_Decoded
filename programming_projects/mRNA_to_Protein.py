#!/usr/bin/python3

"""A simple python script template.
"""

import os
import sys
import argparse


def main(arguments):
    protein = ""
    i = 0
    if len(arguments):
        mRNA = arguments[0]
        RNA_len = len(mRNA)
        
        while i + 2 < RNA_len:            
            # If 1st A
            if mRNA[i] == "A":
                # If AU?
                if mRNA[i + 1] == "U":
                    if mRNA[i + 2] in "UCA":
                        protein += "I"
                    elif mRNA[i + 2] == "G":
                        protein += "start M"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if AC?
                elif mRNA[i + 1] == "C":
                    if mRNA[i + 2] in "UCAG":
                        protein += "T"
                    else:
                        sys.exit("contains invalid nucleotide")
                    
                # if AA?
                elif mRNA[i + 1] == "A":
                    if mRNA[i + 2] in "UC":
                        protein += "N"
                    elif mRNA[i + 2] in "AG":
                        protein += "K"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if AG?
                elif mRNA[i + 1] == "G":
                    if mRNA[i + 2] in "UC":
                        protein += "S"
                    elif mRNA[i + 2] in "AG":
                        protein += "R"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if 2nd not in UCAG
                else:
                        sys.exit("contains invalid nucleotide")

            # if 1st G
            elif mRNA[i] == "G":
                # If GU?
                if mRNA[i + 1] == "U":
                    if mRNA[i + 2] in "UCAG":
                        protein += "V"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if GC?
                elif mRNA[i + 1] == "C":
                    if mRNA[i + 2] in "UCAG":
                        protein += "A"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if GA?
                elif mRNA[i + 1] == "A":
                    if mRNA[i + 2] in "UC":
                        protein += "D"
                    elif mRNA[i + 2] in "AG":
                        protein += "E"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if GG?
                elif mRNA[i + 1] == "G":
                    if mRNA[i + 2] in "UCAG":
                        protein += "G"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if 2nd not in UCAG
                else:
                        sys.exit("contains invalid nucleotide")

            # if 1st U
            elif mRNA[i] == "U":
                # If UU?
                if mRNA[i + 1] == "U":
                    if mRNA[i + 2] in "UC":
                        protein += "F"
                    elif mRNA[i + 2] in "AG":
                        protein += "L"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if UC?
                elif mRNA[i + 1] == "C":
                    if mRNA[i + 2] in "UCAG":
                        protein += "S"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if UA?
                elif mRNA[i + 1] == "A":
                    if mRNA[i + 2] in "UC":
                        protein += "Y"
                    elif mRNA[i + 2] in "AG":
                        protein += "stop"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if UG?
                elif mRNA[i + 1] == "G":
                    if mRNA[i + 2] in "UC":
                        protein += "C"
                    elif mRNA[i + 2] == "A":
                        protein += "stop"
                    elif mRNA[i + 2] == "G":
                        protein += "W"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if 2nd not in UCAG
                else:
                        sys.exit("contains invalid nucleotide")

            # if 1st C
            elif mRNA[i] == "C":
                # If CU?
                if mRNA[i + 1] == "U":
                    if "U" in "UCAG":
                        protein += "L"
                    else:
                        sys.exit("contains invalid nucleotide")
                # If CC?
                elif mRNA[i + 1] == "C":
                    if mRNA[i + 2] in "UCAG":
                        protein += "P"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if CA?
                elif mRNA[i + 1] == "A":
                    if mRNA[i + 2] in "UC":
                        protein += "H"
                    elif mRNA[i + 2] in "AG":
                        protein += "Q"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if CG?
                elif mRNA[i + 1] == "G":
                    if mRNA[i + 2] in "UCAG":
                        protein += "R"
                    else:
                        sys.exit("contains invalid nucleotide")
                # if 2nd not in UCAG
                else:
                        sys.exit("contains invalid nucleotide")

            else:
                sys.exit("contains invalid nucleotide")

            i += 3
       
        print(protein)
            
        

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
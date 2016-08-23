#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#
# File Name:    duplicate_remove.py
#
# Function:     split a file into duplicate lines and unique lines
#
# Usage:        python duplicate_remove.py FILE_IN OUTPUT OUTPUT_DUPLICATE
#
# Input:        FILE_IN: input file
#               OUTPUT: file for unique lines
#               OUTPUT_DUPLICATE: file for duplicate lines
#
# Output:  
#
# Author: panwenhai
#
# Create Time:    2016-08-23 15:18:35
#
######################################################

import sys
import os
import math

reload(sys)
sys.setdefaultencoding('utf-8')

from pybloomfilter import *

def print_help():
    print "USAGE: python duplicate_remove.py FILE_IN OUTPUT OUTPUT_DUPLICATE"

def main():

    if len(sys.argv) != 4:
        print_help()
        return

    file_in = open(sys.argv[1], "r")

    output = open(sys.argv[2], "w")
    output_duplicate = open(sys.argv[3], "w")

    bf = BloomFilter(30000000, 0.0001)

    i = 0
    for line in file_in:
        if i % 10000 == 0:
            print "reading file: %d" % (i)
        i += 1

        line = line.strip()

        if line not in bf:
            bf.add(line)
            output.write(line)
            output.write("\n")
        else:
            output_duplicate.write(line)
            output_duplicate.write("\n")

    return

main()


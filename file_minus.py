#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#
# File Name:    file_minus.py
#
# Function:     remove FILE2's lines from FILE1
#
# Usage:        python file_minus FILE1 FILE2 OUTPUT
#
# Input:        FILE1: source file
#               FILE2: file of minus lines
#               OUTPUT: result file
#
# Output:  
#
# Author: panwenhai
#
# Create Time:    2016-08-23 15:21:50
#
######################################################

#-*-coding: utf-8 -*-

import sys
import os
import math

reload(sys)
sys.setdefaultencoding('utf-8')

from pybloomfilter import *

def print_help():
    print "USAGE: python file_minus FILE1 FILE2 OUTPUT" 

def main():

    if len(sys.argv) != 4:
        print_help()
        return

    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "r")

    output = open(sys.argv[3], "w")

    bf = BloomFilter(300000000, 0.0001)

    i = 0
    for line in file2:
        if i % 100000 == 0:
            print "reading file2: %d" % (i)
        i += 1

        line = line.strip()

        if line not in bf:
            bf.add(line)

    i = 0
    for line in file1:
        if i % 100000 == 0:
            print "reading file1: %d" % (i)
        i += 1

        line = line.strip()

        if line not in bf:
            output.write(line)
            output.write("\n")

    return

main()


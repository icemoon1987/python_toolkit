#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#
# File Name:  attachimg.py
#
# Function:   
#
# Usage:  
#
# Input:  
#
# Output:	
#
# Author: wenhai.pan
#
# Create Time:    2018-04-20 19:18:38
#
######################################################

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import time
from datetime import datetime, timedelta

start_num = int(sys.argv[1])
gap = int(sys.argv[2])
num = int(sys.argv[3])

for i in range(start_num, start_num + gap * num, gap):
    print "[attachimg]%d[/attachimg]" % (i)
    print ""


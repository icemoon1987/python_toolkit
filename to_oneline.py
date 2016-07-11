#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#
# File Name:  cid.py
#
# Function:   
#
# Usage:  
#
# Author: panwenhai
#
# Create Time:    2016-05-20 16:43:10
#
######################################################

from datetime import datetime, timedelta
import time
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


result = []

for line in sys.stdin:
	result.append(line.strip())

print ",".join(result)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#
# File Name:  translate_to_chineses.py
#
# Function:   
#
# Usage:  
#
# Input:  
#
# Output:	
#
# Author: hadoop
#
# Create Time:    2017-06-22 08:36:21
#
######################################################

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import time
from datetime import datetime, timedelta

from googletrans import Translator

translator = Translator()

for line in sys.stdin:
    result = translator.translate(line, dest="zh-CN")

    print result.text



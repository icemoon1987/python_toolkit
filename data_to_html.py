#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#
# File Name:  data_to_html.py
#
# Function:   
#
# Usage:  
#
# Author: panwenhai
#
# Create Time:    2016-06-30 10:28:00
#
######################################################

from datetime import datetime, timedelta
import time
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main ():

	print '<table border="1">'

	for line in sys.stdin:
		ary = line.strip().decode("utf-8").split("\t")
		print "<tr>"
		tmp = "<td>" + "</td><td>".join(ary) + "</td>"
		print tmp
		print "</tr>"
	
	print "</table>"

	return

main()

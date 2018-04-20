#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
#
# File Name:  resize_pics.py
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
# Create Time:    2018-04-20 19:43:53
#
######################################################

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import shutil
import time
from PIL import Image
from datetime import datetime, timedelta


def main():

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    width = int(sys.argv[3])
    watermark = sys.argv[4]

    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    os.mkdir(dst_dir)

    watermark_img = Image.open(watermark)

    for f_name in os.listdir(src_dir):
        print f_name

        image = Image.open(src_dir + "/" + f_name)
        old_width = float(image.size[0])
        old_height = float(image.size[1])

        new_width = width
        new_height = int(width / old_width * old_height)

        resized = image.resize((new_width, new_height), resample=Image.ANTIALIAS)

        #resized.paste(watermark_img, (0, resized.size[1] - watermark_img.size[1]))
        resized.paste(watermark_img, (0, 0))

        resized.save(dst_dir + "/" + f_name, format="jpeg")

    return



if __name__ == "__main__":
    main()

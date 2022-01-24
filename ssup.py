#!/usr/bin/env python3

import random
import string
import sys
import subprocess


filename_length = 4
filetype = ".png"
hostname = "rvdm.net"
path = "screenshots/s/"
urlpath = "https://rvdm.net/s"

def get_random_string(length):
    characters = string.ascii_lowercase + string. ascii_uppercase + string.digits
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str

def copy_file_to_server(source, target):
    subprocess.run(["scp", source, target])

if (sys.argv[1]):
    newfile = get_random_string(filename_length) + filetype
    target = hostname + ":" + path + newfile
    copy_file_to_server(sys.argv[1],target)
    print("%s/%s" % (urlpath,newfile))

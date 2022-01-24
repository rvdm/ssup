#!/usr/bin/env python3

import random
import string
import sys
import subprocess
import os

# set the length of the autogenerated file name
filename_length = 4

# set the file type of your screenshots
filetype = ".png"

# host to scp to
hostname = "rvdm.net"

# path on the host to scp to
path = "screenshots/s/"

# base URL to be prepended to the uploaded file
urlpath = "https://rvdm.net/s"


def get_random_string(length):
    characters = string.ascii_lowercase + string. ascii_uppercase + string.digits
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str

def copy_file_to_server(source, target):
    try:
        subprocess.run(["scp", source, target])
    except subprocess.CalledProcessError as e:
        print("Something went wrong: %s" % e.output)
        sys.exit(1)

if (len(sys.argv) != 2):
    print("Please run this from Automator with one filename to copy as an argument.")
elif (sys.argv[1]):
    newfile = get_random_string(filename_length) + filetype
    target = hostname + ":" + os.path.join(path,newfile)
    copy_file_to_server(sys.argv[1],target)
    print("%s/%s" % (urlpath,newfile))

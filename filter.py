#!/usr/bin/env python

from __future__ import print_function
import subprocess
import sys

def filter_frames(d):
    # get all file names
    out, err = subprocess.Popen(['ls', d],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE).communicate()
    files = filter(bool, out.split('\n'))
    
    # get min/max frame number/name
    max_frame = max(files)
    min_frame = min(files)

    print(min_frame, max_frame)
    
    
                            

def main():
    try:
        # filter_frames(sys.argv[1])
        filter_frames('1')
    except:
        print("Usage: ./filter.py <directory>")
        print("e.g. ./filter.py frames")

if __name__ == '__main__':
    main()

#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    # split the line into words
    features = line.strip().split(',')
    print "%s\t%s\t%s" % (features[0], features[16], features[15]) # (year, airport, delay)
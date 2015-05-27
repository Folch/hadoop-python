#!/usr/bin/env python
import sys

window_size = 500
counter = 0
d = {}
# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	# split the line into words
	features = line.strip().split(',')
	
	year = features[0]
	airport = features[16]
	delay = features[15]
	cancelled = features[21] == "1"
	
	try:
		delay = float(delay)
	except ValueError:
		continue
	
	if not cancelled:
		
		if counter == window_size:
			for y, a in d:
				print "%s,%s\t%s\t%s" % (y, a, d[(y, a)][0], d[(y, a)][1])
			counter = 0
			d = {}
		else:
			if (year, airport) not in d:
				d[(year, airport)] = [delay, 1]
			else:
				d[(year, airport)][0] += delay
				d[(year, airport)][1] += 1
			counter += 1
# flush dict
for y, a in d:
	print "%s,%s\t%s\t%s" % (y, a, d[(y, a)][0], d[(y, a)][1])
	
	
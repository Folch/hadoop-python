#!/usr/bin/env python

from operator import itemgetter
import sys

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	#line = line.strip()
	# parse the input we got from mapper.py
	key, delay, counts = line.split('\t')
	year, airport = key.split(',')
	try:
		delay = float(delay)
		counts = int(counts)
	except ValueError:
		continue
	print '%s\t%s\t%f\t%d' % (year,airport, delay, counts)


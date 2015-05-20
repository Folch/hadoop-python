#!/usr/bin/env python

from operator import itemgetter
import sys

current_airport = None
current_delay = 0
n=0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

    # parse the input we got from mapper.py
	year, airport, delay = line.split('\t', 2)
    
	try:
		delay = float(delay)
	except ValueError:
		continue
	
	if current_airport == airport:
		current_delay += delay
		n += 1
	else:
		if current_airport:
			# write result to STDOUT
			mean = current_delay/n
			print '%s\t%s\t%f' % (year,current_airport, mean)  
		
		n=0
		current_delay = delay
		current_airport = airport

# do not forget to output the last word if needed!
if current_airport == airport:
	mean = current_delay/n
	print '%s\t%s\t%f' % (year,current_airport, mean)


    
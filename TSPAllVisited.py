#!/usr/bin/python

import math, re, sys

# usage: python TSPAllVisited.py input_file output_file

def main(input_file, output_file):
	input_point_labels = read_input_vals(input_file)
	
	output_point_labels = read_output_vals(output_file)
	problems = check_match(input_point_labels, output_point_labels)
	
	
	if( len(problems) == 0):
		print('Each item appears to exist in both the input file and the output file.')
	else:
		print('possible problems include:\n')
		for each in problems:
			print(problems[each])
	
def read_input_vals(in_file):
	# each line of in_file shoudl have a label as its first int on each line,
	# this captures a list of those labels
	# (expected from 0 to n - 1, but only uniqueness is necessary)
	
	file = open(in_file,'r')
	line = file.readline()
	
	#points tracks the points as teh key and the number of visitations as the value at that key
	points = []
	while len(line) > 1:
		line_parse = re.findall(r'[^,;\s]+', line)
		points.append(int(line_parse[0]))
		line = file.readline()
	file.close()
	
	points = sorted(points)
	
	
	return points
	
def read_output_vals(out_file):
	# each line of in_file should have a label as its first int on each line,
	# this captures a list of those labels
	# (expected from 0 to n - 1, but only uniqueness is necessary)
	
	file = open(out_file,'r')
	
	# toss the first line, which should contain a total
	file.readline()
	
	line = file.readline()
	
	
	#points tracks the points as teh key and the number of visitations as the value at that key
	points = []
	while len(line) > 1:
		line_parse = re.findall(r'[^,;\s]+', line)
		points.append(int(line_parse[0]))
		line = file.readline()
	file.close()
	
	points = sorted(points)
	
	return points

def check_match(list_a, list_b):
	problems = dict()
	
	if(len(list_a) != len(list_b) ):
		problems[-1] = ('Different number of points in the files, so they cannot match.')
	
	#smaller = min(len(list_a), len(list_b) )
	offset_a = 0
	offset_b = 0
	problem_count = 0
	while (offset_a < len(list_a) ) and (offset_b < len(list_b) ):
		item_a = list_a[offset_a]
		item_b = list_b[offset_b]
		
		#print(str(item_a) + ', ' + str(item_b) )
		
		if(item_a < item_b):
			problem = (str(offset_a) + ' seems to be missing from the output.')
			problems[offset_a] = problem
			
			offset_a += 1
			problem_count += 1
		elif(item_a > item_b):
			problem = (str(offset_b) + ' seems to be missing from the output.')
			problems[offset_a] = problem
			
			offset_b += 1
			problem_count += 1
		else:
			offset_a += 1
			offset_b += 1
			
	return problems

#if __name__ == '__main__':
	#main(sys.argv[1], sys.argv[2])

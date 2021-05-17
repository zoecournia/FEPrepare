#!/usr/bin/python
import sys

def print_list(sorted_list, prefix):
	for i in range(len(sorted_list)):
		if (prefix == 'MASS'): 
			tokens = sorted_list[i].split(' ')
			print prefix + ' ' + str(i+1) + ' ' + tokens[2] + ' ' + tokens[3] + ' ' + tokens[4]
		else: 
			print sorted_list[i]

def get_name(line):
	if(line.startswith('ATOM')):
		tokens = line.split(' ')
		return tokens[1] + ' ' + tokens[2]
        #if(line.startswith('BOND')):    
	#	tokens = line.split(' ')
	#	return tokens[1] + ' ' + tokens[2]
	else: 
		return line.split(' ')[2]

def merge_lists(filename, dictionary, sorted_list, prefix):
	extra_items = []
	with open(filename) as f:
	    for line in f:
	        line = line.strip()
	        if(not line.startswith(prefix)):
	        	continue

        	name = get_name(line)
	        if(name in dictionary):
	        	new_index = dictionary[name][0]
	        	sorted_list[new_index] = line
	        else:
	        	extra_items.append(line)
        
	return extra_items
   
def create_dictionary(filename, dictionary, prefix):
	index = 0
	with open(filename) as f:
	    for line in f:
	        line = line.strip()
	        if(not line.startswith(prefix)):
	        	continue
	        name = get_name(line)
	        dictionary.update({ name: [index, line] })
	        index += 1

def count_lines(filename, prefix):
	count = 0
	with open(filename) as f:
	    for line in f:
	        line = line.strip()
	        if(not line.startswith(prefix)):
	        	continue
	        count += 1
	return count

def fill_gaps(sorted_list, extra_items):
        
        
	for i in range(len(sorted_list)): 
		if(sorted_list[i] == None):
			sorted_list[i] = extra_items.pop(0) 
                       

fileA = sys.argv[1]
fileB = sys.argv[2]

prefixes = ['MASS', 'ATOM']
for prefix in prefixes: 

	dictionary = {}
	create_dictionary(fileA, dictionary, prefix)

	sorted_list = a = [None] * count_lines(fileB, prefix)
        
	extra_items = merge_lists(fileB, dictionary, sorted_list, prefix)
        
	fill_gaps(sorted_list, extra_items)

	print_list(sorted_list, prefix)

impr=[]
with open(fileB) as f:
  while True:
        lineB = f.readline().strip() 
        if lineB.startswith('BOND'):
            print(lineB)
        if lineB.startswith('IMPR'):
            print(lineB)
        if lineB =='':
            break; 


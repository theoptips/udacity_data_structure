'''
## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python



# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)
'''

import os
import Queue

def find_files(suffix, path):
	if path == "":
		return ""
	if suffix == "":
		return ""
	Q = Queue.Queue()
	Q.enqueue(path)
	suffix = suffix
	result = []
	prefix = ""

	#def find_files_r(Q)
	#"super important to call Q.size() not Q.size in while loop, else NoneType error"

	#1 item added
	while Q.size() != 0: #extremely important to include.size() the ()
		current_path = Q.dequeue()
		if os.path.isfile(current_path):
			if suffix == "*":
				result.append(current_path)
			elif current_path.endswith(suffix):
				result.append(current_path)
		if os.path.isdir(current_path): # if directory entire directory added m directories ms_quare, that's depth of 1 if depth of n is m**(2n) = m^nexponenital
				candidates = os.listdir(current_path)
				for c in candidates:
					c = os.path.join(current_path,c)
					Q.enqueue(c)
	return "\n".join(result)



	# add first to queue
	'''
	build my own queue

	add path to queue 
	while queue not emtpy
	pop from queue as current
	check if current path is a directory or file
	if file check if extension is a match add to result
	if current is a directory list all and add each to queue

	'''
	return os.path.isdir(path)
	pass

test = Queue.Queue()
print(find_files('.c', './testdir'))
#print(find_files('.h', './testdir'))
#print(find_files('.gitkeep', './testdir'))
#print(find_files('*', './testdir'))

assert find_files('', './testdir') == ""
assert find_files('.c', '') ==""
assert len(find_files('.c', './testdir').split("\n")) == 4
assert len(find_files('.h', './testdir').split("\n")) == 4
assert len(find_files('.gitkeep', './testdir').split("\n")) == 2
assert len(find_files('*','./testdir').split("\n"))==10

# Discussion on O(n) calculation:
# ANSWER
# assume max directory or file number in a directory is m including the root
# assume maximum depth of directory is n
# even though there is no actual limit
# but let's assume that it is not reasonable 
# for even messy 
# entperise file wont have more than 100 nested directory deep depth
# but can have upwards of 10000 files in a directory 
# each directory can have m = 10,000 files, so one layer is 10,000*1, but some of these files have 
# sub directories so m*m we can have m extra files for each of the m file in this directory
# as it gets deeper we have (m*m) ** n = m ** (2*n) m to the 2nth power
# which is very high so let's assume that it is m**n m^n which is exponoential
# thankfully, we can just track a huge list of files and directories in a Queue
# it is still possible to handle because of this extra space data structure

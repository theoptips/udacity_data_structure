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

	while Q.size() != 0: #extremely important to include.size() the ()
		current_path = Q.dequeue()
		if os.path.isfile(current_path):
			if current_path.endswith(suffix):
				result.append(current_path)
		if os.path.isdir(current_path):
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
print(find_files('.h', './testdir'))
print(find_files('.gitkeep', './testdir'))

assert find_files('', './testdir') == ""
assert find_files('.c', '') ==""
assert len(find_files('.c', './testdir').split("\n")) == 4
assert len(find_files('.h', './testdir').split("\n")) == 4
assert len(find_files('.gitkeep', './testdir').split("\n")) == 2

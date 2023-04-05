#!/usr/bin/env python3


import os
import sys

prog_name = sys.argv[0]
command_name = sys.argv[1]


#input is 'c'
def create_file():
	print('Creating a file ')
	#Create files from the remaining input stream
	remaining_stream = sys.argv[2:]
	print('Create new archive tape from the following files: ')
	
	#Bytearray to hold our input
	output_stream = bytearray()
	try:
		for file_name in remaining_stream:
			if(os.path.exists(file_name)):
				output_stream += (f'len(file_name):02d'.encode())
				output_stream += (f'{file_name}'.encode())
				#Fix format for st_size
				output_stream += (f'{file_name.st_size}:08d'.encode())
				output_stream += (os.read(file_name, file_name.st_size))
				
			else:
				print(file_name + ' doesn\'t exist')
	except:
		os.write(2, f'One of the files could not be archived.\nPlease try again.'.encode())
		
#input is 'x'
def extract_file():
	print('Extracting a file ')
	#Get path as last input
	extract_path = sys.argv[-1]
	print('Extract from the folowing path ')
	
	#Split the stream of the whole file
	stream = read(extract_path, extract_path.st_size)
	
	#Get the name from 2 bytes
	name_size = 2
	
	#Get the size from 8 bytes
	file_size = 8
	
	while stream:
		#Loop until there are no remaining bytes
		file_name_length = int(stream[:name_size].decode())
		stream = stream[name_size:]
		
		file_name = stream[:file_name_length].decode()
		stream = stream[file_name_length:]
		
		single_file_size = int(stream[:file_size].decode())
		stream = stream[file_size:]
		
		file_cont = stream[:single_file_size]
		os.write(file_name, file_cont)
		
		stream = stream[single_file_size:]
		
	
		

	
	
if(command_name == 'c'):
	create_file()
elif(command_name == 'x'):
	extract_file()

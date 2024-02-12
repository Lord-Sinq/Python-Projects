# open an existing file in the read mode
infile = open('../input/fileslecture/hello_message.txt','r')
print('Opened a file in read mode')

# read whatever is stored in the file
infile_contents = infile.read()

# cloase the file
infile.close()
print('Closed the file!')

# show whatever was read from the file
print(infile_contents)
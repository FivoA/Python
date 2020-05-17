import os 
query = str(input('Whats the name of the text file you would like to check for in this directory? \n'))
if os.path.exists(query):
    print('This file exists.')
else: 
    print('This file does not exist in the directory your running this script in, sorry')
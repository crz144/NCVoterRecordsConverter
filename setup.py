#The purpose of this script is to acquire the necessary files and set
#up the proper file structure for the convert.py script to execute.
import os
import urllib.request as request

if not os.path.exists('./CSVFiles'):                                # Creates ./CSVFiles if it doesn't
     os.mkdir('./CSVFiles')                                         # exist in the directory

list = ["%.3d" % i for i in range(81)]                              # Populates a list with numbers 0-80
                                                                    # in the form "000, 001, 002" etc.

for urlCompleter in list:                                           # Main loop: Acquires all files from the
                                                                    # URLs and places them in ./CSVFiles
    print('Downloading voter_roll_' + urlCompleter + '.csv')
    request.urlretrieve('http://www.cs.unc.edu/Courses/comp89h-f18/Data/voter_roll_' + urlCompleter + '.csv',
                    './CSVFiles\\voter_roll_' + urlCompleter + '.csv')

print("Downloads finished, run convert.py to finish conversions")
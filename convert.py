import csv
import glob
import time
import os
start_time = time.time()

files = glob.glob('./CSVFiles/*.csv')                  #Creates a list of all .CSV files
                                                       #in the provided directory
fileCount = 0
if not os.path.exists('./OutputFiles'):
    os.mkdir('./OutputFiles')
for file in files:                                     #Top level loop: Iterates through all
                                                       #inputted .csv files
    fileCount += 1
    with open(file, 'r', newline='') as inputfile:     #Opens the current file in read-mode

        print("Opening " + file + "...")
        inputreader = csv.reader(inputfile)            #Initializing the .csv reader
        next(inputreader)                              #These lines are necessary to
        row1 = next(inputreader)                              #account for the weird headers
        if file != "./CSVFiles\\voter_roll_080.csv":   #each of the files had.
            row1 = next(inputreader)
        targetCounty = row1[1]
        outputfile = open("./OutputFiles/voter_roll_"
                          + targetCounty + ".csv", 'a+', newline='') #Opens or creates an output
                                                                     #file in append mode.

        outputwriter = csv.writer(outputfile)          #Initializing a csv writer
        print("Writing to " + targetCounty + ".csv")
        rowsPassed = 0
        for row in inputreader:                        #Lower for loop: Iterates over
            rowsPassed += 1                                           # every row in the current file
            if file == "./CSVFiles\\voter_roll_080.csv" and (rowsPassed % 2 == 1):
                    continue
            try:
                currentCounty = row[1]                 #Catches blank rows or
            except IndexError:                         #misc. formatting errors.
                continue

            if currentCounty != targetCounty:          #Transitions to a new output
                                                       #file if a different county is
                                                       #beginning to be evaluated.
                print('New County Reached: Now Writing to ./OutputFiles/voter_roll_' + currentCounty + ".csv")
                outputfile.close()
                targetCounty = currentCounty
                outputfile = open("./OutputFiles/voter_roll_" + targetCounty + ".csv", 'a+', newline='')
                outputwriter = csv.writer(outputfile)
                outputwriter.writerow(row)
                targetCounty = row[1]
                continue
            else:
                outputwriter.writerow(row)
                targetCounty = row[1]

        print("File finished after evaluating " + str(rowsPassed) + " lines")
        outputfile.close()

print("Completed. Total input files evaluated: " + str(fileCount))
if fileCount == 0:
    print("It seems like you forgot to give me any .csv files :(")
elapsed_time = time.time() - start_time
print("Conversion completed after " + str(elapsed_time) + " seconds.")
import sys

fileName = sys.argv[1]
fileName = fileName.encode("string-escape")
myfile = open(fileName, "r+")
myfile.truncate()
myfile.close()

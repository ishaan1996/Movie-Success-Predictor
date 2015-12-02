import sys

import numpy
import random
from sklearn import linear_model
from sklearn import svm
from glb import *
from functions import *
from model import *

inputData = []

def predictSuccess(movieNameList):
	
	movieName = ""
	for name in movieNameList:
	    movieName = movieName + name + " " # dealing with movies with multiple words 
	print movieName

	# DATA CLEANING

	inputFeature = getFingerPrint(movieName)

	line = inputFeature

	for l in range(len(line)):
	    if(l == 22):
	        continue

	    elif(line[l] != ''):
	        line[l] = float(line[l])
	        inputData.append(line[l])


	clf = constructModel()


	prediction = int(clf.predict(inputData))

	if(prediction == 0):
	    print "BLOCKBUSTER"
	elif(prediction == 1):
	    print "CRITICAL WINNER"
	elif(prediction == 2):
	    print "COMMERCIAL VENTURE"
	else:
	    print "HORRIBLE"
	# TEST

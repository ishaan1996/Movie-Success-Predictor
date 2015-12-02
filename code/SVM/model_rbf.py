import numpy
import random
from sklearn import linear_model
from sklearn import svm
from sklearn.svm import SVR
import matplotlib.pyplot as plt

m = {0: 0, 1: 0, 2: 0, 3: 0}


def constructModel():
    inputData = []
    targetData = []
    trainingData = []
    trainingTarget = []
    testData = []
    testTarget = []
    cnt = 0
# DATA CLEANING
    with open('data.txt', 'r') as f:
        for line in f:
            line = line.rstrip().split(",")
            cnt += 1
            subData = []
            subTarget = []
#	    print line

            if(int(line[33])) > 3:
                line[33] = 3
            m[int(line[33])] += 1

            for l in range(len(line)):
                if(l == 22):
                    continue

                if(l + 2 == len(line)):
                    line[l] = float(line[l])
                    targetData.append(line[l])
                elif(line[l] != ''):
                    line[l] = float(line[l])
                    subData.append(line[l])
            inputData.append(subData)

    indices = random.sample([i for i in range(len(inputData))], 100)

    for i in range(len(inputData)):
        if i not in indices:
            trainingData.append(inputData[i])
        else:
            testData.append(inputData[i])
    for i in range(len(targetData)):
        if i not in indices:
            trainingTarget.append(targetData[i])
        else:
            testTarget.append(targetData[i])
    cnt=0
#    clf = svm.SVC()
#    clf2 = linear_model.LogisticRegression()
    clf = svm.SVR(kernel='rbf', C=10, gamma=0.01)
#    svr_lin = svm.SVR(kernel='linear', C=1e3)
#    svr_poly = svm.SVR(kernel='poly', C=1e3, degree = 2)
#    print "svr done"
    clf.fit(trainingData, trainingTarget)
#y_lin=svr_lin.fit(trainingData, trainingTarget)
#    svr_poly.fit(trainingData, trainingTarget)
#    print "y done"
#   plt.scatter(trainingData, trainingTarget, c='k', label='data')
#   plt.hold('on')
#    plt.plot(trainingData, y_rbf, c='g', label='RBF model')
   # plt.plot(X, y_lin, c='r', label='Linear model')
#    plt.plot(X, y_poly, c='b', label='Polynomial model')
#    plt.xlabel('data')
#    plt.ylabel('target')
#    plt.title('Support Vector Regression')
#    plt.legend()
#    plt.show()
    for i in range(len(testData)):
       if(int(clf.predict(testData[i])) == testTarget[i]):
            cnt += 1

    # TEST
    print cnt
    return clf
constructModel()

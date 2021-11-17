import numpy as np
import math
#Input: the lists of prior probabilities, likelihood, and test data
#Output: list of corresponding posterior probabilities
#
def posteriorFunc(priorProb, likhd, data):
    r = []
    sum = 0
    lime_counter = 0
    for i in range(0, len(data)) :
        if data[i] is 1 :
            lime_counter = lime_counter + 1
    for i in range(0, len(priorProb)):
        r.append ((likhd[i] ** lime_counter) * priorProb[i])
        sum = sum + r[i]
    alpha = 1 / sum
    posProb = r
    for i in range(0, len(priorProb)):
        posProb[i] = alpha * r[i]   
    '''
       
       Student implements the function to calculate posterior probabilities here
       
	'''
    return posProb

#Input the lists of prior probabilites, likhd/likelihood, training data, and one test datapoint
#Output: probability that the test datapoint happens
#Note: this function will call posteriorFunc to calculate the posterior probabilites 
def predictionFunc (priorProb, likhd, data, fPoint):
    temp = posteriorFunc(priorProb, likhd, data)
    predictProb = 0                                                                                                                                                                                                           
    for i in range (0, len(priorProb)) : 
        predictProb = predictProb + temp[i] * likhd[i] * fPoint
    '''
       
       Student implements the function to calculate predictive probability here
       
	'''
    return predictProb
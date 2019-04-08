import csv
import random
import math
import operator



path = "Iris.csv"

def loadDataset(filename, split, trainingSet =[] , testSet = []):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(1,len(dataset)):
            for y in range(5):
                dataset[x][y]  =  float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x][1:])
            else:
                testSet.append(dataset[x][1:])
                   

def euclideanDistance(i1 , i2 , length):
    distance =0 
    for x in range(length-1):
        distance += pow(i1[x] - i2[x], 2)
    return math.sqrt(distance)    

       
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist =euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors    

       
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] +=1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]        
        
def getAccuracy(testSet, Predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == Predictions[x]:
            correct +=1       
    return (correct/len(testSet)) * 100.0        
    
def main():
    trainingSet = []
    testSet = []
    split = 0.70
      
    loadDataset(path, split, trainingSet, testSet)
    
    
    predictions = []
    k = 3
    
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x],k)
        result = getResponse(neighbors)
        predictions.append(result)
        print("> Predicted =" + result + " actual=" + testSet[x][-1])
          
    accuracy = getAccuracy(testSet, predictions)
    print(repr(accuracy))

main()

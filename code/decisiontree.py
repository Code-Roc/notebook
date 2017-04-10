# -*- coding: gbk -*-
#Original From:http://blog.csdn.net/alvine008/article/details/37760639
#compatible both in python2 and python3
#use json to make the output tree look better
import math
import json
import operator
def calcShannonEnt(dataSet):  #������Ϣ��
    #calculate the shannon value  
    numEntries = len(dataSet)  
    labelCounts = {}  
    for featVec in dataSet:      #create the dictionary for all of the data  
        currentLabel = featVec[-1]  
        if currentLabel not in labelCounts.keys():  
            labelCounts[currentLabel] = 0  
        labelCounts[currentLabel] += 1  
    shannonEnt = 0.0  
    for key in labelCounts:  
        prob = float(labelCounts[key])/numEntries  
        shannonEnt -= prob*math.log(prob,2) #get the log value  
    return shannonEnt


def splitDataSet(dataSet, axis, value):  #����axis=0��value=���̣��ͻ�õ����������̵���Щ����ɾȥ���������Ľ��
    retDataSet = []  
    for featVec in dataSet:  
        if featVec[axis] == value:      #abstract the fature  
            reducedFeatVec = featVec[:axis]  
            reducedFeatVec.extend(featVec[axis+1:])  
            retDataSet.append(reducedFeatVec)  
    return retDataSet


def chooseBestFeatureToSplit(dataSet):  
    numFeatures = len(dataSet[0])-1  
    baseEntropy = calcShannonEnt(dataSet)  
    bestInfoGain = 0.0; bestFeature = -1  
    for i in range(numFeatures):  
        featList = [example[i] for example in dataSet]  
        uniqueVals = set(featList)  
        newEntropy = 0.0  
        for value in uniqueVals: 
            subDataSet = splitDataSet(dataSet, i , value)  #��������i=0,value=���̣���õ����̵�6����¼��subDataSet
            prob = len(subDataSet)/float(len(dataSet))  
            newEntropy +=prob * calcShannonEnt(subDataSet)  
        infoGain = baseEntropy - newEntropy  
        if(infoGain > bestInfoGain):  
            bestInfoGain = infoGain  
            bestFeature = i  
    return bestFeature


def majorityCnt(classList):  
    classCount = {}  
    for vote in classList:  
        if vote not in classCount.keys(): classCount[vote] = 0  
        classCount[vote] += 1  
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  
    return sortedClassCount[0][0]


def createTree(dataSet, labels):  
    classList = [example[-1] for example in dataSet]  #����б�ÿ�С��ǡ�����
    # the type is the same, so stop classify  
    if classList.count(classList[0]) == len(classList):  #������ȫ�����ǡ��ǡ��򡰷񡱣�return
        return classList[0]  
    # traversal all the features and choose the most frequent feature  
    if (len(dataSet[0]) == 1):#����Ϊ�գ������������
        return majorityCnt(classList)  
    bestFeat = chooseBestFeatureToSplit(dataSet)  #ѡ����õĻ�������
    bestFeatLabel = labels[bestFeat]  
    myTree = {bestFeatLabel:{}}  
    del(labels[bestFeat])  
    #get the list which attain the whole properties  
    featValues = [example[bestFeat] for example in dataSet]  
    uniqueVals = set(featValues)  
    for value in uniqueVals:  
        childDataSet = splitDataSet(dataSet, bestFeat, value)
        if childDataSet == []: 
            myTree[bestFeatLabel][value] = majorityCnt(classList)
        else: myTree[bestFeatLabel][value] = createTree(childDataSet, labels[:])  
    return myTree


def classify(inputTree, featLabels, testVec):  
    firstStr = list(inputTree.keys())[0]
    #firstStr = (inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():  
        if testVec[featIndex] == key:  
            if type(secondDict[key]).__name__ == 'dict':  
                classLabel = classify(secondDict[key], featLabels, testVec)  
            else: classLabel = secondDict[key]  
    return classLabel


dataSet = [
"����,����,����,����,����,Ӳ��,��".split(','),
"�ں�,����,����,����,����,Ӳ��,��".split(','),
"�ں�,����,����,����,����,Ӳ��,��".split(','),
"����,����,����,����,����,Ӳ��,��".split(','),
"ǳ��,����,����,����,����,Ӳ��,��".split(','),
"����,����,����,����,�԰�,��ճ,��".split(','),
"�ں�,����,����,�Ժ�,�԰�,��ճ,��".split(','),
"�ں�,����,����,����,�԰�,Ӳ��,��".split(','),
"�ں�,����,����,�Ժ�,�԰�,Ӳ��,��".split(','),
"����,Ӳͦ,���,����,ƽ̹,��ճ,��".split(','),
"ǳ��,Ӳͦ,���,ģ��,ƽ̹,Ӳ��,��".split(','),
"ǳ��,����,����,ģ��,ƽ̹,��ճ,��".split(','),
"����,����,����,�Ժ�,����,Ӳ��,��".split(','),
"ǳ��,����,����,�Ժ�,����,Ӳ��,��".split(','),
"�ں�,����,����,����,�԰�,��ճ,��".split(','),
"ǳ��,����,����,ģ��,ƽ̹,Ӳ��,��".split(','),
"����,����,����,�Ժ�,�԰�,Ӳ��,��".split(','),
]
labels = "ɫ��,����,����,����,�겿,����".split(',')  
myTree = createTree(dataSet,labels[:])  
print(json.dumps(myTree,indent=4, ensure_ascii=False))#������4��ʾ�����
print(classify(myTree,labels,"����,����,����,�Ժ�,�԰�,��ճ".split(',')))#����һ��δ֪���������������

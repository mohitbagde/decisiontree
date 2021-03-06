import math

#find item in a list
def find(item, list):
    for i in list:
        if item(i): 
            return True
        else:
            return False

#find most common value for an attribute
def majority(attributes, data, target):
    #find target attribute
    valFreq = {}
    #find target in data
    index = attributes.index(target)
    #calculate frequency of values in target attr
    for tuple in data:
        if (valFreq.has_key(tuple[index])):
            valFreq[tuple[index]] += 1 
        else:
            valFreq[tuple[index]] = 1
    max = 0
    major = ""
    for key in valFreq.keys():
        if valFreq[key]>max:
            max = valFreq[key]
            major = key
    return major

#Calculates the entropy of the given data set for the target attr
def entropy(attributes, data, targetAttr, i):

    valFreq = {}
    posFreq = {}
    negFreq = {}
    dataEntropy = 0.0
  #  print targetAttr
    #find index of the target attribute
  #  i = 0
   # for entry in attributes:
    #    if (targetAttr == entry):
    #        break
    #    i=i+1
  #  print i
    # Calculate the frequency of each of the values in the target attr
    for entry in data:
        #print entry[len(attributes)-1]
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            valFreq[entry[i]]  = 1.0
  #  print valFreq
    for entry in data:
        if entry[len(attributes)-1] == 'Yes':
            if (posFreq.has_key(entry[i])):
                posFreq[entry[i]] += 1.0
            else:
                posFreq[entry[i]] = 1.0
        else:
            if (negFreq.has_key(entry[i])):
                negFreq[entry[i]] += 1.0
            else:
                negFreq[entry[i]] = 1.0

    # Calculate the entropy of the data for the target attr
  #  print valFreq
    for i,j,k in zip(valFreq, posFreq, negFreq):
   #     print valFreq, valFreq[i], posFreq[j], negFreq[k]
     #   if(posFreq[j] == 0):
      #      dataEntropy 
        dataEntropy = -(valFreq[i]/len(data) * 
        (posFreq[j]/valFreq[i]*math.log(posFreq[j]/valFreq[i],2)) 
        + (negFreq[k]/valFreq[i]* math.log(negFreq[k]/valFreq[i],2)))
#    for freq in valFreq.values():
      #   print valFreq, freq, len(data), freq/len(data)
      #   print (-freq/len(data)) * math.log(freq/len(data), 2) 
  #       dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
      #   print valFreq,dataEntropy
      #   print dataEntropy
    return dataEntropy

def gain(attributes, data, attr, targetAttr):
    """
    Calculates the information gain (reduction in entropy) that would
    result by splitting the data on the chosen attribute (attr).
    """
    valFreq = {}
    subsetEntropy = 0.0
    posFreq = {}
    negFreq = {}
    #find index of the attribute
    i = attributes.index(attr)
    # Calculate the frequency of each of the values in the target attribute
    for entry in data:
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            valFreq[entry[i]]  = 1.0
   # print valFreq
    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occuring in the training set.
#    print valFreq
    for entry in data:
      #  print entry[len(attributes)-1]
        if entry[len(attributes)-1] == 'Yes':
            if (posFreq.has_key(entry[i])):
                posFreq[entry[i]] += 1.0
            else:
                posFreq[entry[i]] = 1.0
        else:
            if (negFreq.has_key(entry[i])):
                negFreq[entry[i]] += 1.0
            else:
                negFreq[entry[i]] = 1.0
    for val in valFreq.keys():
        valProb        = valFreq[val] / sum(valFreq.values())
        dataSubset     = [entry for entry in data if entry[i] == val]
     #   print len(dataSubset)
        logfunc = entropy(attributes, dataSubset, targetAttr, i)
  #      print val, valProb, logfunc, len(dataSubset)
        subsetEntropy += valProb * logfunc
  #      print "child", val, subsetEntropy 
 ##   print valFreq, subsetEntropy
    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    p = sum(posFreq.values())/ sum(valFreq.values())
    n = sum(negFreq.values())/ sum(valFreq.values())

    entropyParent =  -(p*math.log(p,2)+ n*math.log(n,2))
    entropyGain = entropyParent - subsetEntropy
   # print "gain due to attribute",attr,"=", entropyGain
    return entropyGain

#choose best attibute 
def chooseAttr(data, attributes, target):
    best = attributes[0]
    maxGain = 0;
    for attr in attributes[:-1]:
        newGain = gain(attributes, data, attr, target) 
		#print those attributes that have the sameGain
        if newGain==maxGain:
			print "same information gain ", maxGain, attr, best
        if newGain>maxGain:
            maxGain = newGain
            best = attr
   # print 'highest gain attribute is ',best
    return best

#get values in the column of the given attribute 
def getValues(data, attributes, attr):
    index = attributes.index(attr)
    values = []
    for entry in data:
        if entry[index] not in values:
            values.append(entry[index])
    return values

def getExamples(data, attributes, best, val):
    examples = [[]]
    index = attributes.index(best)
    for entry in data:
        #find entries with the give value
        if (entry[index] == val):
            newEntry = []
            #add value if it is not in best column
            for i in range(0,len(entry)):
                if(i != index):
                    newEntry.append(entry[i])
            examples.append(newEntry)
    examples.remove([])
    return examples

def makeTree(data, attributes, target, recursion):
    recursion += 1
    #Returns a new decision tree based on the examples given.
    data = data[:]
    vals = [record[attributes.index(target)] for record in data]
    default = majority(attributes, data, target)
    # If the dataset is empty or the attributes list is empty, return the
    # default value. When checking the attributes list for emptiness, we
    # need to subtract 1 to account for the target attribute.
    if not data or (len(attributes) - 1) <= 0:
        return default
    # If all the records in the dataset have the same classification,
    # return that classification.
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        # Choose the next best attribute to best classify our data
        best = chooseAttr(data, attributes, target)
        print "parent node = ", best
        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object--we'll fill that up next.
        tree = {best:{}}
        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        for val in getValues(data, attributes, best):
            print "child node =",val
            # Create a subtree for the current value under the "best" field
            examples = getExamples(data, attributes, best, val)
            newAttr = attributes[:]
            newAttr.remove(best)
            subtree = makeTree(examples, newAttr, target, recursion)
         	# Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][val] = subtree
	return tree


import math
import collections
classes = []
totalatts = []

def calcentropy(feature,c):
	sum = 0
	totalinf = 0
	for i in set(feature):
	        sum = sum + c[i]
	for i in set(feature):
	        p = float(c[i])/ float(sum)
	        #print "logp=",math.log(p,2)
	        #print "p=",p
	        totalinf = totalinf+ p*math.log(p,2)
	entropy = abs(totalinf)
	return entropy

def calcinfgain(temparr, classes, ct, i):
	weightedsum = 0
	for j in set(temparr):
        	newtemparr = []
	        count = 0
		for k in range(0, len(totalatts)):
		      if totalatts[k][i] == j:
	#	               print totalatts[k][len(line1)-1]
		               newtemparr.append(totalatts[k][len(line1)-1])
		               count = count+1
	        frac = float(count)/float(len(totalatts))
                #print frac
		c = collections.Counter(newtemparr)
		entperattrib= calcentropy(newtemparr,c)
		weightedsum = weightedsum + frac*entperattrib
	entropybefore = calcentropy(classes,ct)
	entropyafter = entropybefore - weightedsum
	#print entropyafter
	return entropyafter

def id3(R, C, S):
#	 function ID3 (R: a set of non-categorical attributes,
#		 C: the categorical attribute,
#		 S: a training set) returns a decision tree;
#   begin

#	If S is empty, return a single node with value Failure;
#	If S consists of records all with the same value for 
#	   the categorical attribute, 
#	   return a single node with that value;
#	If R is empty, then return a single node with as value
#	   the most frequent of the values of the categorical attribute
#	   that are found in records of S; [note that then there
#	   will be errors, that is, records that will be improperly
#	   classified];
#	Let D be the attribute with largest Gain(D,S) 
#	   among attributes in R;
#	Let {dj| j=1,2, .., m} be the values of attribute D;
#	Let {Sj| j=1,2, .., m} be the subsets of S consisting 
#	   respectively of records with value dj for attribute D;
#	Return a tree with root labeled D and arcs labeled 
#	   d1, d2, .., dm going respectively to the trees 
#
#	     ID3(R-{D}, C, S1), ID3(R-{D}, C, S2), .., ID3(R-{D}, C, Sm);
 #  end ID3;
 	return 1



f = open('dt-data.txt','r')
fdata = f.read()
data = fdata.split('\n')

line1 = data[0].strip("()").split(",")
print line1
for i in data[2:]:
	temp = i[4:].strip(";").split(",")
	temp = [i.strip(" ") for i in temp]
	print temp
	totalatts.append(temp)
	#right now doing for only one attribute 
for k in range(0, len(totalatts)):
	classes.append(totalatts[k][len(line1)-1])
ct = collections.Counter(classes)
print classes
# calc max gain
maxgain = 0.0
maxattrib = 0
for i in range(len(line1)-1):
	temparr = []
	for k in range(0, len(totalatts)):
		temparr.append(totalatts[k][i])
	newgain = calcinfgain(temparr,classes,ct,i)
	print newgain
	if maxgain < newgain:
		maxgain = newgain
		maxattrib = i
print 'max gain =',maxgain, 'best attrib = ', maxattrib, line1[maxattrib]









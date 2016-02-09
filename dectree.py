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
	if maxgain < newgain:
		maxgain = newgain
		maxattrib = i
print 'max gain =',maxgain, 'best attrib = ', line1[maxattrib]









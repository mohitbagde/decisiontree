import DecisionTree
import pprint
import time

def rulegen(d, p):
  for k, v in d.iteritems():
    if isinstance(v, dict): 
        p1 = p
        p = p +" "+k+ " , "
        rulegen(v, p)
        p = p1
    else:
        print "IF",p, k,"THEN", v
    
def main():
    #Insert input file
    file = open('dt-data.txt')
    #class attribute
    target = "Enjoy"
    data = [[]]
    for line in file:
        #cleaning the data
        line = line.strip("\r\n;:0123456789\t").replace(" ","")
        data.append(line.split(',') )
    data.remove([])
    attributes = data[0]
   # attributes = attributes.strip("()")
    attributes = [x.strip("()") for x in attributes]
   # need to pass only the non-target attributes without any attribute headers and that one empty line
    data.remove(data[0])
    data.remove(data[0])
   # Run ID3
    print "Generated decision tree"
    tree = DecisionTree.makeTree(data, attributes, target, 0)
    pp = pprint.PrettyPrinter(indent = 4, depth = 14)
    pp.pprint(tree)
    #Generate IF THEN rules
    print "if - then rules"
    pre = ""
    rulegen(tree, pre)
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
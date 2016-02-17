import DecisionTree
import pprint

def main():
    #Insert input file
    file = open('WeatherTraining.csv')
    #class attribute
    target = "play"
    data = [[]]
    for line in file:
        #cleaning the data
        line = line.strip("\r\n;:0123456789\t").replace(" ","")
        data.append(line.split(',') )
    data.remove([])
    attributes = data[0]
   # attributes = attributes.strip("()")
    attributes = [x.strip("()") for x in attributes]
  #  print attributes
    #need to pass only the non-target attributes without any attribute headers and that one empty line
    data.remove(data[0])
  #  data.remove(data[0])
    #Run ID3
   # print data
    tree = DecisionTree.makeTree(data, attributes, target, 0)
    pp = pprint.PrettyPrinter(indent = 4, depth = 14)
    pp.pprint(tree)
    print "generated decision tree"
    #Generate program
   
    
    
if __name__ == '__main__':
    main()
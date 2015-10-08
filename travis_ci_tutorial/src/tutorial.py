#!/usr/bin/env python
import os, sys, getopt, json


def sum_elements(elements):
    #return sum(int(i) for i in elements)
    result = 0;
    for element in elements:
        result = element
    return result

def main():

    usage1 = "travis-ci-tutorial -f <json-file>" 
    usage2 = "travis-ci-tutorial -s <json-string>" 
    data = None  
    try:
        opts, args = getopt.getopt(sys.argv[1:],"f:")
    except getopt.GetoptError:
      print "Usage:"
      print "\t",usage1
      print "\t",usage2
      sys.exit(2)
    
    for opt, arg in opts:
        if '-f' == opt:
            with open(arg) as data_file:    
                data = json.load(data_file)

    if data is None:
        print "Data must be specified"

    try:
       print sum_elements(data['elements'])
    except Exception, e:
        print "An error occurs while procesing JSON: ", e
        sys.exit(4)





if __name__ == "__main__":
    main()

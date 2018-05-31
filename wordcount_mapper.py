import sys             #a python module with system functions for this OS

for line in sys.stdin:  
    line = line.strip()  #strip is a method, ie function, associated
                         #  with string variable, it will strip 
                         #   the carriage return (by default)
    keys = line.split()  #split line at blanks (by default), 
                         #   and return a list of keys
    for key in keys:     #a for loop through the list of keys
        value = 1        
        print('{0}\t{1}'.format(key, value) ) #the {} is replaced by 0th,1st items in format list
                            #also, note that the Hadoop default is 'tab' separates key from the value


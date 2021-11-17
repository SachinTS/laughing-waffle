import sys
from itertools import zip_longest

def cmp(a, b):
    # https://docs.python.org/3/reference/expressions.html#value-comparisons
    return (a > b) - (a < b)

def verCompare( v1, v2):
        # create a list of integer for both versions
        v1, v2 = map(int, v1.split('.')), map(int, v2.split('.'))

        #create tuple with adjacent and fill 0 for the reminder
        v1, v2 = zip(*zip_longest(v1, v2, fillvalue = 0))
        # compare the list of tuples
        return cmp(v1,v2)

v1 = sys.argv[1]
v2 = sys.argv[2]

result = verCompare(v1,v2)
#print(["equal", v1 + " greater than " + v2, v2 + " greater than " + v1][result])

print(result)

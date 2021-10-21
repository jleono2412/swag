import  sys


s= sys.argv[1]
result =eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
print (sys.argv[1])
print(result)




#func2.py

#Scoping Rule(Rule of scoping)

x=1
######### func1 ###########
#define
def func1(a):
    return a+x

#call
print(func1(1))


######### func2 ###########
#define
def func2(a):
    x=5
    return a+x

#call
print(func2(1))


#case(have default value)
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

#Keyword arameter(using name)
def connectURI(server, port):
    strURI = "https://" + server + ":" + port
    return strURI

print(connectURI("multi.com","80"))
print(connectURI(port="8080", server="multi.com"))

#Variable Count Argument
def union(*ar):
    #local value
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "SPAM"))
print(union("HAM","SPAM","EGG"))

#Lambda(Once Function)
g = lambda x,y:x*y
print(g(3,4))

print( (lambda x:x*x)(3) )
print( globals() )
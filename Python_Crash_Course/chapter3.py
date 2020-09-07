# Chapter 3 _ Introducing Lists

## Length Of List Start ##
print("-- Length Using Loop --")
bus=['hanif','shyamoly','desh travels','BRTC',"2423"]

for i in range(0,len(bus)):
    print(i)
## Length Of List End ##

print("")
print("")

## Adding Elements to a List (Appending Elements to the End of a List) Start ##
print("-- Append --")
name = ['omar','lutfa','faruk','biki','kaium','abir','shafin']
name.append('riajul')
print(name)
## Adding Elements to a List (Appending Elements to the End of a List) End ##

print("")
print("")

## Insert Elements into a List (Any Position) Start ##
print("-- Insert --")
name2 = ['omar','lutfa','faruk','biki']
name2.insert(2,'arafat ullah nur')
print(name2)
## Insert Elements into a List (Any Position) End ##

print("")
print("")

## Removing Elements from a List (Removing an Item by Value) Start ##
print("-- Removing Elements --")
bus=['hanif','shyamoly','desh travels','BRTC',"2423"]
bus.remove("hanif")
print(bus)
## Removing Elements from a List (Removing an Item by Value) End ##

print("")
print("")

## Removing an Item Using the pop() Method (Popping Items from any Position in a List) Start ##
print("-- Removing an Item Using pop() --")
bus=['hanif','shyamoly','desh travels','BRTC','mtcl',"2423"]
mehedi=bus.pop(1)
print(mehedi)
print(bus)
## Removing an Item Using the pop() Method (Popping Items from any Position in a List) End ##

print("")
print("")

## Removing an Item Using the del Statement Start ##
print("-- Removing an Item Using del --")
bus=['hanif','shyamoly','desh travels','BRTC',"2423"]
del bus[0]
print(bus)
## Removing an Item Using the del Statement End ##

print("")
print("")

## Sorting a List Permanently with the sort() Method Start ##
print("-- Sorting Permanently Using sort() --")
bus=['hanif','shyamoly','desh travels','BRTC',"2423"]
bus.sort()
print(bus)
## Sorting a List Permanently with the sort() Method End ##

print("")
print("")

## Sorting a List Temporarily with the sorted() Function Start ##
print("-- Sorting Temporarily Using sorted() --")
bus=['hanif','shyamoly','desh travels','BRTC',"2423"]
lis=[]
lis=sorted(bus)
print(lis)
print(bus)
## Sorting a List Temporarily with the sorted() Function End ##

print("")
print("")

## Printing a List in Reverse Order Start ##
print("-- Reverse Order --")
bus=['hanif','shyamoly','desh travels','BRTC',"2423"]
bus.reverse()
print(bus)
## Printing a List in Reverse Order End ##

print("")
print("")

## Finding the Length of a List Start ##
print("-- Length of List --")
bus=['hanif','shyamoly','desh travels','BRTC',"2423"]
l=len(bus)
print(bus)
print(l)
## Finding the Length of a List End ##

# Chapter 5 _ If Statements

buses=['hanif','shyamoly','desh travels','BRTC',"ena","thikana"]
favouritebuses=['BRTC','hanif']

## A Simple Example
# for bus in buses:
#     if bus == 'shyamoly':
#         print(bus.upper())
#     else:
#         print(bus.title())


## Testing Multiple Conditions
# for i in buses:
#     if i=="BRTC":
#         print(i,"It is govt company")
#     elif i=="hanif":
#         print(i,"This is my favorite coach")
#     else:
#         print(i,"It is private company")

# for i in buses:
#     if "ena" not in buses:
#         print("so sad")


## Using Multiple Lists
# for favouritebus in favouritebuses:
#     if favouritebus in buses:
#         print(favouritebus + ", Book my ticket")
#         break
#     else:
#         print("Don't book my ticket")


## Checking for Special Items
# for bus in buses:
#     if bus == 'shyamoly':
#         print("Sorry, we are out of service right now.")
#     else:
#         print("Available " + bus + ".")
# print("Confirmed!")
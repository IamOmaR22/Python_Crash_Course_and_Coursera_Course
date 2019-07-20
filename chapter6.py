# Chapter 6 _ Dictionaries

# print("16-05-2019")
# print("Today we learn about python dictionary")

## A Simple Dictionary (Accessing Values in a Dictionary)
# dress = {'color':'green','points':5}
# print(dress['color'])
# print(dress['points'])

## Dictionary
# first_dict={'name':'Omar','age':'22','city':'dhaka','subject':'cse','id':8709,'cgpa':'3.75'}
# print("Student name: ", first_dict['name'])
# print("Student age: ", first_dict['age'])
# print("Student id: ", first_dict['id'])
#
# first_dict={'name':'Mehedi'}
# print("Student name: ",first_dict['name'])
# print("Student age: ", first_dict['age'])
# print("Student id: ", first_dict['id'])


## Adding New Key-Value Pairs
# first_dict['credit'] = 13
# first_dict['p_a'] = 'Shukrabad'
# print(first_dict)


## Modifying Values in a Dictionary
# first_dict['name']='mehedi'
# first_dict['id']=8421
# print("\nstudent name: ", first_dict['name'])
# print("student age: ", first_dict['age'])
# print("student id: ", first_dict['id'])


## Empty Dictionary
# emptydict={}
# emptydict['sunday'] = 'beef'
# emptydict['monday'] = 'fish'
# emptydict['tuesday'] = 'egg'
# emptydict['wednesday'] = 'vegetable'
# emptydict['thursday'] = 'chicken'
# print(emptydict['sunday'])
# print(emptydict['tuesday'])
# print(emptydict)


## Removing Key-Value Points
# meal = {'breakfast':'Bread','launch':'chicken','dinner':'fish'}
# print(meal)
# del meal['launch']
# print(meal)


## Looping Through a Dictionary (Looping Through All Key-Value Pairs)
# signup = {'first_name':'omar','last_name':'faruk','username':'omar22'}
# for key, value in signup.items():  # .items() is necessary
#     print("\nkey: "+ key)
#     print("value: "+ value)

## Looping Through All Keys in a Dictionary
# for key in signup.keys():  # .keys() is not necessary
#     print(key.title())

## Looping Through a Dictionary's Keys in Order
# languages = {'bangladesh':'bengali','kolkata':'bangla','mumbai':'hindi','usa':'english','saudi':'arabic'}
# for key in sorted(languages.keys()):  # .keys() is not necessary
#     print(key.title())

## Looping Through All Values in a Dictionary
# for value in languages.values():
#     print(value.title())

## Nesting (A List of Dictionaries)
# paracetamol = {'ace':'square','fast':'acme','aceta':'biopharma'}
# cetirizine = {'acitrin':'aci','cetrin':'drug','alatrol':'square'}
# omeprazole = {'cosec':'drug','losectil':'eskayef','prevas':'general'}
# medicines = [paracetamol,cetirizine,omeprazole]
# for medi in medicines:
#     print(medi)

## Make an Empty List for Storing Medicines
# medicines = []
# for medic in range(50):
#     omep = {'cosec':'drug','losectil':'eskayef','prevas':'general'}
#     medicines.append(omep)
# for medi in medicines[:6]:  # [:6] means, 6 out of 50 will show
#     print(medi)
# print("...")  # ... means
# print("Total number of medicines: " + str(len(medicines)))


## A List in a Dictionary
# restaurant={'mac&spicy':'pasta','sultan':['kacchi','biriyani'],'chillox':'pizza','cafe_sim_sim':'platter','kfc':'chicken fry','dominos':'pizza','shwarma_king':'shwarma','mama_halim':'halim','star_kabab':'kabab','pasta_state':'pasta','prince':'faluda'}
# print(restaurant['sultan'])
# print("Foods are:")
# for food in restaurant['sultan']:
#     print( food)


## A Dictionary in a Dictionary (** Key must be same **)
# bf_gf = {'ba':{'bf':'biki','gf':'annesa','location':'gopalgang'},'km':{'bf':'kaium','gf':'momo','location':'keranigang'},}
# for couple, couple_info in bf_gf.items():
#     print("\nCouple  Username: " + couple)
#     couple_name = couple_info['bf'] + " " + couple_info['gf']
#     location = couple_info['location']
#     print("\tCouple Name: " + couple_name)
#     print("\tLocation: " + location)


## A Dictionary in a Dictionary (** Key must be same **) Example: 2
# many_drugs = {'paracetamol':{'square':'ace','location':'dhaka'},'omeprazole':{'square':'seclo','location':'cumilla'},}
# for medicine, medi_info in many_drugs.items():
#     print("\nDrug Name: " + medicine)
#     medicine_name = medi_info['square']
#     location = medi_info['location']
#     print("\tMedicine Name: " + medicine_name)
#     print("\tLocation: " + location)


# restaurant={'mac&spicy':'pasta','sultan':'kacchi','chillox':['pizza','burger'],'cafe_sim_sim':'platter','kfc':'chicken fry','dominos':'pizza','shwarma_king':'shwarma','mama_halim':'halim','star_kabab':'kabab','pasta_state':'pasta','prince':'faluda'}
# count=0
# count2=0
# res=input("Enter restaurant name:").lower()
# food=input('Enter food name:')
# for key, value in restaurant.items():
#     count2=count2+1
#     if key == res:
#         if food in restaurant[key]:
#             # if item == food:
#                  print("Sir please come to our restaurant, your food is available now.")
#             #      break
#         else:
#             print("This food is unavailable")
#     else:
#         count=count+1
# if count==count2:
#     print("There is no restaurant")

#
# food_resturant = {'pasta':'cafe_darbar','pizza':'dominos','kacchi':'sultan'}
# choose_food = input("Enter the food name: ")
# for key, value in food_resturant.items():
#     if key in choose_food:             # key means food and value means restaurant
#         amount = input("Enter your amount: ")
#         a = int(amount)
#         if a >= 0 and a <= 100:
#             print("Restaurant name is " + value + " . " + "Please come sir, Your food is available")
#         else:
#             print(value)  # value means, we just want to show restaurant name ,not full dict
#             print("Restaurant name is " + value + "." + "Sorry sir, Your food is not available")


dict= = {
  "brand":"Ford", 
  "model":"Mustang",
  "year": 2021
}
#used to store data values in key:value pairs
#dictionary is a collection which is ordered, changeable and do not allow duplicates.

print(dict)

#presented in key:value pairs, and can be referred to by using the key name.

print(dict["brand"])

#dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

#dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#dictionaries cannot have two items with the same key.

#to determine how many items a dictionary has, use the len() function

print(len(dict))

#the values in dictionary items can be of any data type.

dict = {
  "tea":"green",
  "hot": True,
  "year": 2000,
  "colors": ["red", "blue"]
}
#Python's perspective - dictionaries are defined as objects with the data type 'dict'.

print(type(dict))

#output - <class 'dict'>
#it is also possible to use the dict() constructor to make a dictionary.

thisisdict = dict(name = "John", age = 15, country = "USA")
print(thisisdict)

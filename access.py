#we can access the items of a dictionary by referring to its key name, inside square brackets

dict = {
  "car":"BMW",
  "year": 1999
}
x = dict["year"]
print(x)

#get() will give you the same results

x = dict.get("year")

#keys() will return all keys in dictionary

x = dict.keys()

#values() method will return a list of all the values in the dictionary.

x = dict.values()

#items() method will return each item in a dictionary, as tuples in a list.

x = dict.items()

#to determine if a specified key is present in a dictionary use the "In" keyword

if "year" in dict:
   print("It is inside")



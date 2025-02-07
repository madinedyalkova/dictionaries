#you can change the value of a specific item by referring to its key name.

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["year"] = 2018

#update() method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with key:value pairs.

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.update({"year":2010})

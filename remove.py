#pop() method removes the item with the specified key name

dict = {
  "car": "Ford"
  "year" : 2020
  }
dict.pop("car")
print(dict)

#popitem() method removes the last inserted item

dict.popitem()
print(dict)

#del keyword removes the item with the specified key name

dict = {
  "car": "Ford"
  "year" : 2020
  }

del dict["car"]
print(dict)

#del also delete the dictionary

del(dict)

#clear() method empties the dictionary
dict = {
  "car": "Ford"
  "year" : 2020
  }
dict.clear()

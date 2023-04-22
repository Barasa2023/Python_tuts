#python dictionaries
#dictionaries are unordered collection of key value pairs
prices = {"apples":30, "mangoes":10, "oranges":10}

#items can be accessed using their keys
#add an item

prices["pineapples"] = 300
print(prices)

#print all values and keys
print(prices.keys())
print(prices.items())
print(prices.values())

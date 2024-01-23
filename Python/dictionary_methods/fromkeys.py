x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)
thisdict['key1'] = 2
print(thisdict)

y = ["Kiran", "Ishan", "Rohan"]
thatdict = dict.fromkeys(y)
print(thatdict)

thatdict["Kiran"] = 4
print(thatdict)
d= [0,1,2,3,4]
print(d)

if 1 in d:
    print("Number present")
else:
    print("Number not Present")

slice = d[1:]
print(slice)

if 0 in slice:
    print("Number present")
else:
    print("Number not Present")

slice = {"name": "sunil", "array" :[1,2,3,4]}
print(slice)

if "name" in slice:
    print("Name present")
else:
    print("Name not Present")

del(slice["name"])

print(slice)    
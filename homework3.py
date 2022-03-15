mydict = {"net": 3, "farm": 45, "bench": 33, "goal": 60 }
for k,v in mydict.items():
    if v % 3 == 0:
        mydict[k] = "Hi"
    if v % 5 == 0:
        mydict[k] = "Bye"
   
print(mydict)


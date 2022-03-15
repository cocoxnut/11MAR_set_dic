months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
months = months_a.union(months_b)
print(months)
months.add("Dec")
print(months)
for i in months:
    print(i)

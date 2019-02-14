def last_four(x):
    return x[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
new_ids = []
for c in ids:
    new_ids.append(str(c))

sorted_ids = []
for  a in sorted(new_ids, key=lambda x:last_four(x)):
    sorted_ids.append(int(a))
print(sorted_ids)



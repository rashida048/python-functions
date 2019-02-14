ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
def last_four(x):
    return x[-4:]
string1 = []
for i in ids:
    string1.append(last_four(str(i)))
string1 = sorted(string1)
new_ids = []
for id in ids:
    new_ids.append(str(id))
sorted_ids=[]
for s in string1:
    for i in new_ids:
        if s in i:
            sorted_ids.append(int(i))               
print (sorted_ids)


sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for l in sally:
    if l not in characters:
        characters[l] = 0
    characters[l] += 1
li = list(characters.keys())
worst_char = li[0]
for w in li:
    if characters[w] < characters[worst_char]:
        worst_char = w
print (worst_char)




def stop_at_four(list): 
    new_list = []
    i = 0
    while i < len(list):
        if list[i] == 4:
            return new_list
        else:
            new_list.append(list[i])
        i += 1
    return new_list





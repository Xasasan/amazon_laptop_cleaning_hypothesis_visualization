llist = [1, 10, 3, 7]
abc = 0
for i in llist:
    abc += i
    if i <= abc:
        abc = i
    else:
        abc = i
print(abc)




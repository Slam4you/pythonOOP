n = int(input())
mydict = {}
all_parents_dict = {}
for i in range(n):
    str = input().split(':')
    print(str)
    if len(str) == 1:
        mydict[str[0]] = []
    else:
        mydict[str[0].strip()] = str[1].strip().split()
print(mydict)

for key, value in mydict.items():
    all_parents_dict[key] = []
    if len(mydict[key]) == 0:
        continue
    else:
        for i in mydict[key]:
            all_parents_dict[key].append(i)
            if i in mydict.keys() and mydict[i] != [] and len(mydict[i]) == 1:
                all_parents_dict[key].append(*mydict[i])
            elif i not in mydict.keys():
                continue
            else:
                all_parents_dict[key].extend(mydict[i])

print('ALL ->', all_parents_dict)

m = int(input())
for i in range(m):
    str = input().split()
    print(str)
    if str[1] not in all_parents_dict.keys():
        print('No')

    elif str[0] in all_parents_dict[str[1]]:
        print(str[1], 'value--->', all_parents_dict[str[1]])
        print('Yes')
    # elif mydict[str[0]] == []:
    # print(str[1], 'value--->', mydict[str[1]])
    # print('Yes')
    else:
        print(str[1], 'value--->', all_parents_dict[str[1]])
        print('No')
    """2

A : C B

B : D E

1

E A




4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A"""

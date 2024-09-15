from itertools import permutations
a = input()
b = permutations(a,1)
c = permutations(a,2)
d = permutations(a,3)
for items in b:
    print(items[0],end=" ")
print()
for items in c:
    e = "".join(items)
    print(e,end=" ")
print()
for items in d:
    f = "".join(items)
    print(f,end=" ")

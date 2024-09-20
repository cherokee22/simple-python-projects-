
''' the duplicate list items and printing the non repeated ones '''
a = list(input("enter the items"))
dup=[]
def repeat(a):
 for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
              dup.append(a[j])
 print(dup)

print(repeat(a))
print(set(a)-set(dup))

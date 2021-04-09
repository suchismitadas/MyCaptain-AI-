n=int(input("Enter the no of items in the list"))
list=[]
print("enter the items of the list")
for i in range(n):
    item=input(":")
    list.append(int(item))

for items in list:
    if items<0:
        list.remove(items)

print(list)


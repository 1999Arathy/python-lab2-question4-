#Write a python program to count repeated characters in a string.

#lst = []
str =input("enter a str")
'''lst = list(str)
lst2=[]
x=len(lst)
#print("lst2 : ",lst2)
for x in lst:

    if x not in lst2:
        lst2.append(x)
        print(x)

y =len(lst2)
print(lst2)'''

count = {}.fromkeys(str,0)

for char in str:
    if char in count:
        count[char] +=1
print(count)



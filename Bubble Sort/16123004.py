l = [2,3,4,5,6,8]
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    l.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(l[j] > l[j + 1]):
             temp = l[j]
             l[j] = l[j + 1]
             l[j + 1] = temp

print("The Sorted List in Ascending Order : ", l)


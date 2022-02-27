#q-1
print('Q-1')
print('Tower of Hanoi with 3 disks')
def hanoitower(a,x,y,z):
#base case
    if a==1:
        print('Replace 1st disk from',x,'to',z)
        return
    hanoitower(a-1,x,z,y)
    print('Replace',a,'th disk from',x,'to',z)
    hanoitower(a-1,y,x,z)
#calling the function
hanoitower(3,'1','2','3')

#q-2 
print("Q-2)Pascal's triangle for n number of rows given by the user")
rows=int(input('Enter number of rows-'))
#using iteration
print("Output using iteration:")
lista=[]
for i in range(rows):
    list1=[]
    for j in range(i+1):
#base case        
        if j==0 or j==i:
            list1.append(1)
        else:
            list1.append(lista[i-1][j-1] + lista[i-1][j])
    lista.append(list1)

for i in range(rows):
    for j in range(rows-i-1):
        print(format(" ","<2"),end="")
    for j in range(i+1):
        print(format(lista[i][j],"<3"),end=" ")
    print()
#using recursion
print("Output using Recursion:")

def pascal(rows,x=rows):
    if rows==0:
        return
    pascal(rows-1,x)
    print(' '*(x-rows),end='')
    c=1
    for i in range(1,rows+1):
        print(c,end=' ')

        c=c*(rows-1//i)
    print()
pascal(rows)    
   

#q3 
print('Q-3')
#taking values from user
x=float(input('Enter 1st number-'))
y=float(input('Enter 2nd number-'))
q,r=divmod(x,y)
print("Quotient=",q)
print("Remainder=",r)
tup1=(x,y,q,r)
#calling the function
print('Part A)callable-',callable(divmod),".The function/values is callable")
#non zero values
print('Part B)')
if x==0 or y==0 or q==0 or r==0:
    print("All values are not non zero")
else:
    print("All values are non zero")
#part c
res=(q,r)+(4,5,6)
print('Part C)Appending values-',res)
filt=filter(lambda x:x<=4,res)
tup=tuple(filt)
print('Part C)Filtering values greater than 4-',tup)
#part d
set1=set(tup)
print('Part D)Set=',set1)
#part e frozenset
set2=frozenset(set1)
print('Part E)Immutable set-',set2)
#part f
print('Part F)Max value-',max(set1))
print('Part F)Hash value-',hash(max(set1)))

#q4
print('Q-4')
#creating class and assigning values
class student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def details(self):
        print('Details:Name-',self.name,',Roll Number-',self.roll_number)
student1=student("Aditya",4)
student1.details()
#deleting object
del student1
print('Deleting the object-student1')


#q5
print('Q-5')
#creating class
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print('Details:Name-',self.name,',Salary-',self.salary)
e1=employee("Mehak",40000)
e2=employee("Ashok",50000)
e3=employee("Viren",60000)
e1.details()
e2.details()
e3.details()
#part a
e1.salary=70000
print('Part A)Updating the salary of Mehak-')
e1.details()
del e3
print('Part B)Deleted the record of employee viren')

#q6
print('Q-6')
#taking word input from user
from itertools import permutations
word=str(input('Enter the word uttered by George'))
m=str(input('Enter the word uttered by Barbie'))
lst=[''.join(p) for p in permutations(word)]
print(lst)

#to check if Barbie's word matches with any of the possible answers
if m in lst:
    print('Your friendship is real')
else:
    print('Your friendship is fake')






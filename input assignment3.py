#q-1 
print('Q-1')
string=input('Enter the input string-')
words=string.split()
#counting occurances of each character in the input string
if len(words)==1:
 for ch in string:
     print(ch,'=',string.count(ch))
#counting occurances of each word in the input string
else:
  for word in words:
      print(word,'=',words.count(word))

#q2
print('Q-2')
#taking input for year 
year=int(input('Enter Year[1800-2025]-'))
#condition for leap year
if (year%4==0):
    leapyear=True
#for non leap years    
else:
    leapyear=False
#taking input for month
month=int(input('Enter Month[1-12]-'))
if month in (4,6,9,11):
    days=30
#for february month    
elif month==2:
    if leapyear:
        days=29
    else:
        days=28
#for other months
else:
    days=31
#taking input for day
day=int(input('Enter Date[1-31]-'))
#changing the date entered
if day<days:
    day+=1
#if last day of the year
if day==31:
    if month==12:
        month=1
        year+=1
        day=1
    else:
        month+=1
print('The next date is(dd,mm,yyyy):',day,"-",month,"-",year)        

#q3 
print('Q-3')
#taking input from user to create input list
lst=[]
n=int(input('Enter number of elements:'))
for i in range(0, n):
    ele=int(input('Enter list element-'))
    lst.append(ele)
print('Input list=',lst)    
#squaring the elements of the list
b=[i**2 for i in lst]
#zipping numbers and their squares
print('Output:',list(zip(lst,b)))

#q4
print('Q-4')
#taking grade input from user
g=float(input('Enter a grade between 4 and 10-'))
##usinf if else to print output
if g==10:
    print('Your Grade is "A+" and Outstanding Performance.')
elif g>=9:
    print('Your Grade is "A" and Excellent Performance.')
elif g>=8:
    print('Your Grade is "B+" and Very Good Performance.')
elif g>=7:
    print('Your Grade is "B" and Good Performance.')
elif g>=6:
    print('Your Grade is "C+" and Average Performance.')
elif g>=6:
    print('Your Grade is "C+" and Average Performance.')
elif g>=5:
    print('Your Grade is "C" and Below Average Performance.')
elif g>=4:
    print('Your Grade is "D" and Poor Performance.')
else:
    print('Error-Your Grade is out of range')

#q5
print('Q-5')
line='ABCDEFGHIJK'
length=len(line)
for i in range(length):
    for j in range(i):
        print(" ",end="")
    for j in range(length-2*i):
        print(line[j],end="")
    print()    

#q6
print('Q-6')
#repeatedly asking user for input
d={}
while True:
 name=input('Enter name-')
 sid=input('Enter SID-')
 d[sid]=name
 p=input('Do you want to add more elements in the list?(Use "Y" for yes and "N" for no)')
 if p=='Y':
     continue
 elif p=='N':
     break
#part A
print('A)Student details =',d)
#part B sort using values
dic=sorted((value,key) for (key,value) in d.items()) 
dic2=dict([(k,v) for v,k in dic])
print('B)Sorted dictionary using student names-',dic2)
#part C sort using keys
print('C)Sorted dictionary using SID-')
for i in sorted(d):
    print((i,d[i]),end=",")
print()
#part D 
sid_=input('Enter SID from the dictionary to search for the corresponding name-')
print('D)Print name of student using SID-',(sid_,d[sid_]))

#q7
print("Q-7")
#take input from user for no. of terms
n=int(input('Enter number of terms-'))
#defining fibonacci function
def fibonacci(n):
    a=0
    b=1
    if n<=0:
        print("Invalid")
    elif n==1:
        print(n)
    else:
        print(a,end=",")
        print(b,end=",")
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=",")
    return (" ")            
print(fibonacci(n)) 
#average of resultant fibonacci sequence
#defining function for sum of fibonacci series 
def fibsum(n):
    if n==0 or n==1:
        print(n)
    else:
        sum=0
        a=0
        b=1
        sum=a+b
        for i in range(0,n-2):
            c=a+b
            sum+=c
            a=b
            b=c
        
    return(sum)
#printing the sum
print('Sum of fibonacci series-',fibsum(n))
x=fibsum(n)
print('Average of the above fibonacci numbers-',(x)/n)

#q8
print('Q-8')
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
print(Set1)
print(Set2)
print(Set3)
#part a
print('A)Set of elements that are in set1 and set2 but not in both-',Set1^Set2)
#part b
print('B)Set of elements that are in only one of the three sets-',Set1^Set2^Set3)
#part c
print('C)Set of elements that are exactly two of the sets set1,set2 and set3-',Set1&Set2|Set2&Set3|Set3&Set1)
#part d
print('D)Set of all integers in the range 1 to 10 that are not in set1-',set(range(1,10))-Set1)
#part e
print('E)Set of all integers in the range 1 to 10 that are not in set1,set2 and set3-',set(range(1,10))-Set1-Set2-Set3)




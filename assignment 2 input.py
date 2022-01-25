#q1 
print('Q-1')
python='Python is a case sensitive language'
print(python)
print('Length of the string=',len(python))
# reversing 
print('Reversed order of the string=',python[::-1])
#storing-'a case sensitive' in a new string
slice=python[10:26]
print('New string containing-"a case sensitive"=',slice)
#replacing 
print('Replacing "a case sensitive" with "object oriented"')
new=python.replace("a case sensitive","object oriented")
print(new)
#finding index of a
index=python.find("a")
print('Index of "a"=',index)
#removing white spaces in string 
print('Removing all the white spaces in the string=',python.replace(" ",""))

#q2 string formatting
print('Q-2')
name='Lakshanya jindal'
sid=21104054
dept='Electrical engineering'
cgpa=9.9
print("Hey,%s Here!"%(name))
print("My SID is %d"%(sid))
print("I am from %s department and my CGPA is %s" %(dept,cgpa))

#q3 bitwise operators
print('Q-3')
a=56
b=10
print("a=",a,"b=",b)
print('Part A) a&b=',a&b)
print('Part B) a|b=',a|b)
print('Part C) a^b=',a^b)
print('Part D) left shift a with 2 bits=',a<<2)
print('Part D) left shift b with 2 bits=',b<<2)
print('Part E) right shift a with 2 bits=',a>>2)
print('Part E) right shift b with 4 bits=',b>>4)

#q4 finding greatest of 3 numbers
print('Q-4')
x=float(input('Enter no.1='))
y=float(input('Enter no.2='))
z=float(input('Enter no.3='))
if (x>y) and (x>z):
    print('Greatest no. is=',x)
elif (y>x) and (y>z):
    print('Greatest no. is=',y)
else:
    print('Greatest no. is=',z) 
    
#q5 substring in string
print('Q-5')
x=input('Enter string-')
print('Is "name" present in the input string:')
if 'name' in x:
    print("YES")
else:
    print("NO")
    
#q6sides of a triangles
print('Q-6')
x=int(input('Enter side 1-'))
y=int(input('Enter side 2-'))
z=int(input('Enter side 3-'))
if x>y+z:
    print('Can you form a triangle-','NO')
elif y>x+z:
    print('Can you form a triangle-','NO')
elif z>x+y:
    print('Can you form a triangle-','NO')
else:
    print('Can you form a triangle-','YES')
    
        





print('PYTHON ASSIGNMENT 1')
#q1
print('Q1')
x=float(input('Enter no.1-'))
y=float(input('Enter no.2-'))
z=float(input('Enter no.3-'))
a=(x+y+z)/3
print('Average is', a)
#Q2
print('Q2')
g=float(input('Enter gross income-$'))
d=int(input('Enter no. of dependents-'))
x=g-10000-(3000*d)
y=x/5
print('Tax', '=$' ,y)
#Q3
print('Q3')
sid=int(input('Enter SID-'))
name=str(input('Enter Name-'))
gender=input('Enter Gender(F,M,U-FOR UNKNOWN)-')
course=input('Enter Course name-')
cgpa=float(input('Enter CGPA-'))
details=[sid,name,gender,course,cgpa]
print('Student',details)
#Q4
print('Q4')
a=float(input('Enter marks of student 1-'))
b=float(input('Enter marks of student 2-'))
c=float(input('Enter marks of student 3-'))
d=float(input('Enter marks of student 4-'))
e=float(input('Enter marks of student 5-'))
marks=[a,b,c,d,e]
marks.sort()
print('Sorted list of marks',marks)
#Q5
print('Q5')
list=['Red','Green','White','Black','Pink','Yellow']
print('color',list)
list.remove('Black')
print('Part A-List after removing 4th element\n',list)
del list[3:4]
list.insert(3,'Purple')
print('Part B-Replacing black and pink with purple\n',list)

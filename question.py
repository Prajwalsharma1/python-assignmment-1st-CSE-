print("question 1")
a=int(input("enter first number:  "))
b=int(input("enter first number:  "))
c=int(input("enter first number:  "))
avg = (a+b+c)/3
print("avg is:",avg)


print("question 2: compute a person's income tax")
gross_income=input("Please enter gross income: ")
gross_income=float(gross_income)
standard_deduction=10000
dependents=input("Enter the no. of dependents: ")
dependents=int(dependents)
#there is a $3000 deduction for each dependents
dependent_deduction=3000

#tax rate=20%
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
print("taxable income:")
print(taxable_income)
tax=(taxable_income*20)/100
print("tax:")
print(tax)


print("question 3:make a list of SID,NAME,GENDER,COURSE NAME,CGPA")
name=input("Please enter name: ")
sid= input("Enter student Id: ")
gender=input("Enter gender: ")
course_name=input("Enter your course name: ")
cgpa=input("Enter cgpa: ")
sid=int(sid)
cgpa=float(cgpa)
#our list now name as student_info
data=['Name','SID','Gender','Course name','Cgpa']
print(data)
student_info=[name,sid,gender,course_name,cgpa]
print(student_info)
 

print("question 4: make a list of marks of 5 students and show them in sorted manner")

student_1marks=int(input("Enter student 1 marks: "))
student_2marks=int(input("Enter student 2 marks: "))
student_3marks=int(input("Enter student 3 marks: "))
student_4marks=int(input("Enter student 4 marks: "))
student_5marks=int(input("Enter student 5 marks: "))

my_list=[student_1marks,student_2marks,student_3marks,student_4marks,student_5marks]
print("List: ")
print(my_list)
print("Sorted List(decreasing order): ")
my_list.sort(reverse=True)
print(my_list)


print("question 5")
print("(a) print a list and then remove 4th element from the list and let it print the new list")
print("(b) remove 'Black' and 'Pink' from the list and replace it with 'Purple'")

my_list=['Red','Green','White','Black','Pink','Yellow']
#(a) part
print('(a)')
print(my_list)
# remove 4th term that is black
my_list.remove('Black')
print(my_list)

my_list=['Red','Green','White','Black','Pink','Yellow']
#(b) part
print('(b)')
print(my_list)
#replace black and pink with purple
# to replace nth term we write {my_list[n-1]='new value'}
my_list[3:5]=['Purple']
print(my_list)

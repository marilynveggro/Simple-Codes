#numbers
a = 8
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print("-------------")

#modulus
a = 8
b = 5
print(a%b)
print("-------------")

#3 numeric type()
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

print("-------------")

#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

print("-------------")

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

print("-------------")
#complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print("-------------")

#add 2 numbers entered
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

print("-------------")

#find the Average of 2 entered
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

average =(int(num1) + int(num2))

print('average:{0} '.format(average))

print("-------------")
#average 3 written grades entered
firstexam = input('your first exam : ')
secondexam = input('your second exam : ')
thirdexam = input('your third exam : ')
average =(float(firstexam)+float(secondexam)+float(thirdexam))/3
print("average :{0} ".format(average))

print("-------------")

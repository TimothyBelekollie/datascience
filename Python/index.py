import statistics



'''print("Please enter any any integer number:")
number =int(input())
if number > 20:
    print('The number is greater than 20')
else:

      print('The number is less than 20')'''
      
      
#elif statements

if 20>2:
    print("The statement is true")
   
elif 20<12:
        print("The statement is not right")
def emoji(unicode=None):
    print(unicode)
    
emoji("\U0001F60E")

def students(*names):
    #names is a tuple with arguments
    for name in names:
        print("Welcome",name)
        
students("Simran","Timothy","John","Paul","Flomo")

# If you do not know how many arguements that will be be passed into your function, add a * before the parameter name in the function definition.

def my_function(*mm):
    for p in mm:
        print(p)
my_function("Hi", 'my name','is','function with loops',5000)

#Lambda Function
def func(a): #normal function
    c=a+10;
    return c;
func(5)

print("This is the lambda")
x=lambda a:a+10
print(x(5))

x=lambda m,n:m**n
print(x(4,2))

def func(n):
    return lambda c:c*n
results=func(3)
print(results(11))


# Python Global variable

a="I am outside function"
def func():
    b="I am inside function"
    return b
func()

def func():
    b='I am inside function'
    full_sentence=b+''+'and'+''+a
    return full_sentence


func()

#Python File
'''
file=open('tim.txt',mode='w',encoding='utf-8')
file.close()'''

#open the file
file=open("tim.txt",mode='w',encoding='utf-8')

#appending the content to the file
file.write('This statement is added just right now to see how too write to a file')

#close the opened the file
#file.close()
file=open('tim.txt','w')
file.write('timbelekoliej')
file.close()
tim=open('tim.txt','r')
print(tim.read())


from datetime import date
print(date.today())




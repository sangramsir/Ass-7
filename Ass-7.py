 # In Python Create a function with a default parameter "file" storing the file path
def f(file="D:\PYTHON\Assignment-7.py"):
    print("The file name is : ",file)
f()
"""
Output of Create a function wiht a default parameter "file" storing the file path :
The file name is :  D:\PYTHON\Assignment-7.py
"""
# In Python Open the file in append mode
f=open("Temp.txt","+a")
f.write("Hi Hello")
print(f.read())
f.close()
"""
Output of Open the file in append mode : 
Hi Hello
"""
# In Python Use writelines() method to add your roll number, name, and class
f1=open("Temp1.txt","a")
f1.writelines(["Roll Number : 98","Name : Sangram","Class : TYCO5I"])
f1.close()
"""
Output of Use writelines() method to add your roll number, name, and class : 
Roll Number : 98Name : SangramClass : TYCO5I
"""
# In Python Use readines() method to print your data in the prompt
f2=open("Temp2.txt","a")
f2.writelines(["Roll Number : 98 ","Name : Sangram ","Class : TYCO5I"])
f2.seek(0)
f2.close()
f3=open("Temp2.txt","r")
print(f3.readline())
f3.close()
"""
Output of Use readines() method to print your data in the prompt : 
Roll Number : 98 Name : Sangram Class : TYCO5I
"""
# In Python Try and Except block without arithmetic error
try:
    a=10
    b=10
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
"""
Output of Try and Except block without arithmetic error:
1.0
"""
# In Python Try and Except block with arithmetic error
try:
    a=10
    b=0
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
"""
Output of Try and Except block with arithmetic error:
This is arithmetic error
"""
# In Python Try and Multiple Except block without arithmetic error
try:
    a=10
    b=10
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
except Exception:
    print("This is exception error")
"""
Output of Try and Multiple Except block without arithmetic error:
1.0
"""
# In Python Try and Multiple Except block with arithmetic error
try:
    a=10
    b=0
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
except Exception:
    print("This is exception error")
"""
Output of Try and Mutliple Except block with arithmetic error:
This is arithmetic error
"""
# In Python Try and Finally block without arithmetic error
try: 
    a=10
    b=10
    print(a/b)
finally:
    print("This is finally block")
"""
Output of Try and Finally block Without arithmetic error:
1.0
This is finally block
"""
# In Python Try and Finally block with arithmetic error
try: 
    a=10
    b=0
    print(a/b)
finally:
    print("This is finally block")
"""
Output of Try and Finally block With arithmetic error:
This is finally block
"""
# In Python Try , Except and Finally block without arithemtic error
try:
    a=10
    b=10
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
finally:
    print("This is finally block")
"""
Output of Try , Except and Finally block without arithemtic error:
1.0
This is finally block
"""
# In Python Try , Except and Finally block with arithemtic error
try:
    a=10
    b=0
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
finally:
    print("This is finally block")
"""
Output of Try , Except and Finally block with arithemtic error:
This is arithmetic error
This is finally block
"""
# In Python Try , Multiple Except and Finally block without arithemtic error
try:
    a=10
    b=10
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
except Exception:
    print("This is Exception error")
finally:
    print("This is finally block")
"""
Output of Try , Muliple Except and Finally block without arithemtic error:
1.0
This is finally block
"""
# In Python Try , Multiple Except and Finally block with arithemtic error
try:
    a=10
    b=0
    print(a/b)
except ArithmeticError:
    print("This is arithmetic error")
except Exception:
    print("This is Exception error")
finally:
    print("This is finally block")
"""
Output of Try , Muliple Except and Finally block with arithemtic error:
This is arithmetic error
This is finally block
"""
"""
Output of Entire program:
The file name is :  D:\PYTHON\Assignment-7.py
Hi Hello
Roll Number : 98Name : SangramClass : TYCO5I
Roll Number : 98 Name : Sangram Class : TYCO5I
1.0
This is arithmetic error
1.0
This is arithmetic error
1.0
This is finally block
This is finally block
1.0
This is finally block
This is arithmetic error
This is finally block
1.0
This is finally block
This is arithmetic error
This is finally block
"""


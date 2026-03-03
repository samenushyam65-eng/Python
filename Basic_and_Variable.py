# Introduction to Basic and Variable in Python

print(3+2)   # addition(+)
print(3-2)   # subtraction(-)
print(3*2)   # multiplication(*)
print(3/2)   # division(/)
print(3**2)  # exponential(**)
print(3%2)   # modulus(%)
print(3//2)  # Floor division operator(//)

# Checking data types

print(type(10))                 # Int
print(type(3.14))               # Float
print(type(1+3j))               # Complex
print(type('Shaym'))            # String
print(type([1,2,3]))            # List
print(type({'name':'shyam'}))   # Dictionary
print(type({9.8,56,4}))         # set
print(type((4,1.2,56)))         # Tuple
print(type(False))              # Bool
print(type(3==3))               # Bool

# Variables in Python

v=5
print(v)

# 5=v                           # SyntaxError: cannot assign to literal
# print(5)                      # we cannot create a variable starting with number
# 5v=6
# print(5v)                     # SyntaxError: invalid syntax    

v5 =6
print(v5)

nit=20                           # NameError: name 'NIT' is not defined,
# print(NIT)                     because variable names are case-sensitive in Python.
print(nit)

# nit$=10                    #syntaxError: invalid syntax,
# print(nit)                 # because variable names cannot contain special characters except _ (underscore).

First_name ='Shyam'
print(First_name)

""" Keywords are reserved words in Python that cannot be used as variable names,
function names, or any other identifiers."""

import keyword
print(keyword.kwlist)            
print(len(keyword.kwlist))        # There are 35 keywords 

# for = 67                  # SyntaxError: invalid syntax
# print(for)                # because 'for' is a reserved keyword in Python.    

FOR = 67
print(FOR)                 # This is valid because variable names are case-sensitive     

"""
-Variable is case sensitive
-Variable does not start with a digit but end with a digit
-Special characters are not allowed except _ (underscore)
-Variable names cannot be the same as keywords
-Out of 35 keywords |True,False and None are start with capital
"""

name= 'Shyam'
Age = 22
Is_Married = False
skills =['Python','SQL','Power BI']
person_info ={'phone': 1234567890, 'email': 'shyam@example.com'}

print('Name:', name)
print('Age:', Age)
print('Married:', Is_Married)
print('Skills:', skills)
print('Person Information:', person_info)

name,Age,Is_Married,skills = 'Shyam', 22, False,['Python','SQL','Power BI']
print('Name:', name)
print('Age:', Age)
print('Married:', Is_Married)
print('Skills:', skills)

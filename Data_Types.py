""" 
Python data types
1. int
2. float    
3. complex
4. string
5. Boolean
"""

i =56
print(i)                    
print(type(i))                # Output: <class 'int'>

f = 3.14
print(f)
print(type(f))                # Output: <class 'float'>
f2 = 2.5e0            # e0 = 10^0 ,e2 = 10^2, e-2 = 10^-2  or E0 = 10^0 ,E2 = 10^2, E-2 = 10^-2
print(f2)                   # Output: 2.5
print(type(f2))             # Output: <class 'float'>

"""Complex numbers are only available in Python and not in other programming languages.
and format of complex number is a + bj, where a is the real part and b is the imaginary part.
In Python, the imaginary part is denoted by 'j' instead of 'i' and (j^2=-1) """
c = 1+3j
print(c)        
print(type(c))                # Output: <class 'complex'>
print(c.real)           # Output: 1.0, real part of the complex number
print(c.imag)           # Output: 3.0, imaginary part of the complex number

print(c.conjugate())    # Output: (1-3j), conjugate of the complex number
print(abs(c))          # Output: 3.1622776601683795, magnitude of the complex number i.e sqrt(a^2 + b^2) where a is the real part and b is the imaginary part of the complex number.
print(abs(-3))          # Output: 3, absolute value of -3  (Remove the negative sign and return the positive value)
print(abs(3))          # Output: 3, absolute value of 3

s = 'Shyam'
print(s)
print(type(s))                # Output: <class 'str'>

""" Concatenation of string variables """
name,Age,Is_Married = 'Shyam', 22, False
print('Name: ' + name + ', Age: ' + str(Age) + ', Married: ' + str(Is_Married)) 
# In pyhon we cannot concatenate string with non-string data types, so we need to convert non-string data types to string using str() function.

b = True
print(b)
print(type(b))               # Output: <class 'bool'> 
print(True+True)             # Output: 2 in python True = 1 and False = 0
print(True+False)
print(True-True)
print(False+False)

print(id(i))               # id() function returns the memory address of the object.
print(type(i))             # type() function returns the type of the object.

4
print(4)               # Output: 4
10
print(10)              # Output: 10
_ +  5
print(_ + 5)      # Output: 15, _ is a special variable that holds the result of the last expression evaluated in the interactive interpreter.


print(10/2)           # Output: 5.0
print(10//2)     # Output: 5
print(False/True)   # Output: 0.0, because False is treated as 0 and True is treated as 1 in arithmetic operations.
print(True/False)   # Output: ZeroDivisionError: division by zero, because False is treated as 0 and division by zero is not allowed in Python.




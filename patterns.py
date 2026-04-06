""" 1. Right Angle Triangle Pattern """
# for i in range(5):
#     print('*'*(i+1))
    
""" 2. Inverted Right Angle Triangle pattern """
# for i in range(5,0,-1):
#     print('*'*i)

""" 3. Pyramid Pattern """
# for i in range(5):
#     print('*'*(2*(i+1)-1))

# for i in range(5):
#     print(" "*(5-i)+'*'*(2*i-1))

""" 4. Inverted Pyramid Pattern """

# for i in range(5,0,-1):
#     print('*'*(2*i-1))

""" 5.Diamond Pattern """
    
# for i in range(1,6):
#     print(" "*(5-i)+'*'*(2*i-1))
# for i in range(4,0,-1):
#     print(" "*(5-i)+ '*'*(2*i-1))

""" 6.Hallow Square pattern """

# for i in range(1,6):
#     if i in [1,5]:
#         print('*'*5)
#     else:
#         print('*'*1+' '*3+'*'*1)

#################################
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == 1 or i == n or j==1 or j==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

""" 7.Full Square Pattern """

# for i in range(5):
#     print(' * '*5)

""" 8.Right Angle triangle (Number Pattern)"""

# for i in range(1,6):
#     for j in range(i):
#         print(j+1,end=' ')
#     print(' ')
    
""" 9.Inverted Right Angle Triangle (Number Pattern)"""

# for i in range(5,0,-1):
#     for j in range(i):
#         print(j+1,end=' ')
#     print(' ')

""" 10.Floyd's triangle """

# a=0
# for i in range(5):
#     for j in range(i):
#         a=a+1
#         print(a,end=' ')
#     print(" ")
    
""" 11.Hallow Right Angle Triangle """

# for i in range(1,6):
#     if i in [1,2]:
#         print('*'*i)
#     elif i ==5:
#         print("*"*i)
#     else:
#         print('*'+' '*(i-2)+'*')

######################################

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         if j==0 or j==i-1 or i ==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

""" 12.Hallow Pyramid Pattern """
# n=5
# for i  in range(1,n+1):
#     if i == 1:
#         print('  '*(n-i)+'*'*i)
#     elif i == n:
#         print('* '*(i+4))
#     else:
#         print('  '*(n-i)+"*"+'  '*(2*i-3)+' *') 

########################################
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if j == 1 or j==2*i-1 or i == n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

""" 13.Hallow Diamond Pattern """
# n=5
# for i in range(1,n+1):
#     if i == 1:
#         print(' '*(n-i)+'*'*i)
#     else:
#         print(" "*(n-i)+"*"+' '*(2*i-3)+"*")    
    
# for i in range(n-1,0,-1):
#     if i==1:
#         print(" "*(n-i)+"*"*i)
#     else:
#         print(' '*(n-i)+'*'+' '*(2*i-3)+'*')

###############################################


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

""" 14.Hallow Diamond (Number Pattern) """
# n=5
# for i in range(1,n+1):
#     if i ==1:
#         print(" "*(n-i)+str(i))
#     else:
#         print(" "*(n-i)+str(i)+' '*(2*i-3)+str(i))
        
# for i in range(n-1,0,-1):
#     if i ==1:
#         print(" "*(n-i)+str(i))
#     else:
#         print(" "*(n-i)+str(i)+' '*(2*i-3)+str(i))

######################################

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print(i,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print(i,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
    
""" 15.Butterfly Pattern """
# n=7
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end=' ')
#     for j in range(1):
#         print(' '*(4*(n+1-i)-4),end='')
#     for j in range(i):
#         print(j+1,end=' ')
#     print()

# for i in range(n,0,-1):
#     for j in range(i):
#         print(j+1,end=' ')
#     for j in range(1):
#         print(' '*(4*(n+1-i)-4),end='')
#     for j in range(i):
#         print(j+1,end=' ')
#     print()



# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(1):
#         print(' '*(4*(n+1-i)-4),end='')
#     for j in range(i):
#         print('*',end=' ')
#     print()

# for i in range(n,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(1):
#         print(' '*(4*(n+1-i)-4),end='')
#     for j in range(i):
#         print('*',end=' ')
#     print()


"""16. Hallow Number Pyramid """
# n=7
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=' ')
        
#     for j in range(1,2*i): 
#         if j==1 or j==2*i-1 or i ==n:  
#             print(i,end=' ')
#         else:
#             print(' ',end=' ')
#     print()

""" 17. Full Star Pyramid """

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=' ')
#     for j in range(2*i-1):
#         print("*",end=' ')
#     print()

""" 18.Inverted Full Star Pyramid """

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(2*i-1):
#         print('*',end=' ')
#     print()
    
""" 19.Left Aligned Pyramid Pattern """

# n= 5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=' ')
#     print()
    
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end=' ')
#     print()

""" 20.Right Aligned Pyramid Pattern """

# n= 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print(j+1,end=' ')
#     print()
    
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print("*",end=' ')
#     print()
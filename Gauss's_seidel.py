#import the liabrary numpy 
import numpy as np
#initailaize the matrix a 
a=[[8,3,-3],
   [-2,-8,5],
   [3,5,10]]

#for absolute values of the matrix that is :
abs_values_of_matrix=np.abs(a)
print(abs_values_of_matrix)

#sum of all the diagnol values pesent in a matrix
diag=np.diag(abs_values_of_matrix)
print("summ of all values of diagnol is: ",diag)

#sum of each all rows present in the matrix  
sumOfRows=np.sum(abs_values_of_matrix,axis=1)
print("sum of each rows of the matrix is: ",sumOfRows)

#print the sum of all off diagnol element 
sumOf_Off_diag=np.sum(abs_values_of_matrix,axis=1)-diag
print("sum of all off diagnol matrix row wise is : ",sumOf_Off_diag)

#condition of diagnol vales is greater than the off diagnol values print the code continue whether the else condition is applied
if np.all(diag>sumOf_Off_diag):
    print("matrix is diagnolly dominant")
else:
    print("matrix is not diagonolly dominant") 


#initial values of x1,x2 and x3
x1=0
x2=0
x3=0

#If the difference between the current and previous iterations is smaller than epsilon, the solution is considered sufficiently accurate, and the iterative process can be terminated.
epsilon=0.001

# refers to the point at which the solution of an iterative process has stabilized and no longer changes significantly with further iterations
converged=False

#The previous values assign in the the x1,x2,x3 is: 
x_old=np.array([x1,x2,x3])
print(x_old)

#maximum iteration till the code run inside the for loop
max_iteration=50

print("iteration result")

print("k         x1        x2        x3   ")

#apply the condtion to definite the range of the lopp from 1 till 50 
for k in range(1,max_iteration):

    x1=(14-3*x2+3*x3)/8
    x2=(5+3*x1-5*x3)/(-8)
    x3=(-8-3*x1-5*x2)/10

#the new matrix will print and storing the each values in x1 ,x2 ,x3
    x=np.array([x1,x2,x3])
    print('%2d            %4f            %4f             %4f'  %  (k,x1,x2,x3))

    #Finally, the square root is taken of the dot product. This gives you the Euclidean distance
    dx=np.sqrt(np.dot(x-x_old,x-x_old))

    if dx<epsilon:
        converged=True
        print("converged")
        break

    x_old=x

    if not converged:
        print("Not converged ,increase the iteration ")   
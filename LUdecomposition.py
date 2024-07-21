#for installing numpy liabrary used the command (pip install numpy)
import numpy as np
from numpy.linalg import inv #imports a specific function, inv, from the linalg (linear algebra) submodule of NumPy.
"NumPy's linalg module provides a collection of functions for performing common linear algebra operations"


#for installing scipy liabrary used the command (pip install scipy)
import scipy
from scipy.linalg import lu
#help(lu)#this line tells about what lu is?

#import the module array from the numpy which convert the input list as an structured array 
A=np.array([
    [1,1,1,1],
    [2,3,1,5],
    [-1,1,-5,3],
    [3,1,7,-2]
], dtype=float)#tells to store the values in form of the float

""""p, l, u =:
The function returns three matrices:"""

""""HERE,lu(A) You call the lu function (from scipy.linalg, as NumPy doesn't have a built-in lu function) and pass
your matrix A as an argument."""

p,l,u=lu(A)

#This print the entire matrix
print("A",A)

#This print the lower values of the matrix
print("L",l)

#This print the upper values of the matrix
print("U",u)

#This print permutation: accounts for any row swaps needed to perform the decomposition
print("p:",p)

y=np.array([10,31,-2,18])

L=p.dot(l)

m=inv(L).dot(y)

x=inv(u).dot(m)

print("\nThe final answer after LU decomposition is: ")
print(x)
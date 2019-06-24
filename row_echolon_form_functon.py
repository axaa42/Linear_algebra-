import sympy
import numpy as np

matrix_one = np.asarray([
[2, -2, 4,-2],
[2, 1, 10,7],[-4,4,-8,4],[4,-1,14,6]  
], dtype=np.float32)

reduced_echolon_form=sympy.Matrix(matrix_one).rref()
#print(reduced_echolon_form)

#Note that accurcay might not be perfect.so double check on internet with a row echolon calculator

matrix_two = np.asarray([
[1,1, -1,7],
[1, -1, 2,3],[2,1,1,9]  
], dtype=np.float32)

reduced_echolon_form2=sympy.Matrix(matrix_two).rref()
#print(reduced_echolon_form2)

#The result returns two tuples.The first is the reduced row echolon form.
#Note column 1=x, column 2=y, column 3=z, column 4=result. 
#We can see that z=-2,y=-1,x=6.
#The second tuple just shows where the 1 in each row are.
matrix_three = np.asarray([
[30,-1,-1000],
[50,-1,-100]  
], dtype=np.float32)

reduced_echolon_form3=sympy.Matrix(matrix_three).rref()
print(reduced_echolon_form3)
import gauss_jordan as gj

matrix1 = gj.Matrix([[1, 2, 3], [4, 5, 6], [0, 0, 1]])
matrix2 = gj.reduced_echelon(matrix1)
matrix2.print()

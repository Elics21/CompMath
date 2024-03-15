def MPI(A, B, x0, epsilon, maxIteration = 50):
     sizeMatrix = len(B)
     x = x0
     countIterations = 1
     flagEpsilon = False
     while (countIterations <= maxIteration) and not flagEpsilon:
          newX = [0] * sizeMatrix
          for i in range(sizeMatrix):
               sum = 0
               for j in range(sizeMatrix):
                    if(j != i):
                         sum += A[i][j] * x[j]
               newX[i] = (B[i] - sum) / A[i][i]

          print(countIterations, end="      | ")
          for i in newX:
               print(f" {i:.5f}", end=" |")
          # Проверяем достижение требуемой точности
          error  =  max(abs(newX[i] - x[i]) for i in range(sizeMatrix))
          if error < epsilon:
               flagEpsilon = True
          x = newX
          countIterations += 1
          print()

A = [[10, 2, -1], [-2, -6, -1], [1, -3, 12]]
B = [5, 24, 36]
x0 = [0, 0, 0]
epsilon = 0.01

# print("A:")
# for i in range(len(B)):
#      for j in range(len(B)):
#           print(A[i][j], end=" ")
#      print()
#
# print("\nB:")
# for i in range(len(B)):
#      print(B[i])
#
# print("\nX0:")
# for i in range(len(x0)):
#      print(x0[i])

print()
print("Number |  x1      |  x2      |  x3     |")
MPI(A, B, x0, epsilon)




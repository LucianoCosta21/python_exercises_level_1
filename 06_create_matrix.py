def create_matrix(M, N):
     return [[i * j for j in range(N)] for i in range(M)]

#print(create_matrix(4,8))


def create_matrix2(M,N):
     matriz = []

     for i in range(M):
          row = []
          for j in range(N):
               row.append(i * j)
          matriz.append(row)
          
     return matriz

print(create_matrix2(4,3))




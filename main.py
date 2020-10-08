from NQueensProblem import NQueensProblem
from hillClimbing import randomRestartHillClimbing
from time import time

def localSearch(problem):
  countLoop = 0
  start = time()
  while True:
    countLoop += 1
    result = randomRestartHillClimbing(problem)
    if problem.heuristicFunc(result) == 0:
      break
  end = time()
  print("* Algoritmo Hill Climbing executado %d vezes" %(countLoop))
  print("* Tempo de execução: %f\n" %(end-start))
  return result

def transformListToMatrix(list, N):
  matrix = [["_" for x in range(N)] for y in range(N)] 
  for c, l in enumerate(list):
    matrix[l][c] = 'R'
  
  return matrix

def printBoard(matrix):
  for l in range(0, len(matrix)):
    for c in range(0, len(matrix)):
      if(matrix[l][c] == '_'):
        print('[ ]', end='')
      else:
        print(f'[{matrix[l][c]}]', end='')
    print()
  print()

def main():
  Ns = [10, 20, 25]
  for N in Ns:
    print("------------------------------------------------------------")
    print("-------------------------- N = %d --------------------------" %(N))
    print("------------------------------------------------------------")
    problem = NQueensProblem(N)    
    listResult = localSearch(problem)
    matrixResult = transformListToMatrix(listResult, N)
    print("Solução encontrada")
    printBoard(matrixResult)

if __name__ == "__main__":
  main()
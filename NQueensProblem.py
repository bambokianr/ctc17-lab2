import random
import collections

class NQueensProblem():
  #! a = line: guarda o valor das linhas das rainhas
  #! b = diag_1: guarda l-c das rainhas
  #! c = diag_2: guarda l+c das rainhas

  def __init__(self, N):
    self.N = N

  def initialState(self):
    return list(random.randrange(0, self.N) for i in range(self.N))

  def heuristicFunc(self, state):
    h = 0
    
    # lineCount = {}
    # diag_1Count = {}
    # diag_2Count = {}
    diag_1Count, diag_2Count, lineCount = [collections.Counter() for i in range(3)]

    for c, l in enumerate(state):
      # diag_1Count[l-c] = diag_1Count.get(l-c, 0) + 1
      # diag_2Count[l+c] = diag_2Count.get(l+c, 0) + 1
      # lineCount[l+c] = lineCount.get(l, 0) + 1
      diag_1Count[l-c] += 1
      diag_2Count[l+c] += 1
      lineCount[l] += 1

    for count in [diag_1Count, diag_2Count, lineCount]:
      for key in count:
        h += count[key] * (count[key]-1) / 2
    
    return -h

  def neighborStates(self, state):
    neighborStates = []

    for l in range(self.N):
      for c in range(self.N):
        if l != state[c]:
          aux = list(state)
          aux[c] = l
          neighborStates.append(list(aux))

    return neighborStates

  def goalTest(self, state):
    diag_1 = []
    diag_2 = []
    line = []
    
    for c, l in enumerate(state):
      if l-c in diag_1 or l+c in diag_2 or l in line:
        return False
      diag_1.append(l-c)
      diag_2.append(l+c)
      line.append(l)
    return True
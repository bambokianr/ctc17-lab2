
def hillClimbing(problem):
  currentState = problem.initialState()
  while True:
    neighborStates = problem.neighborStates(currentState)
    if not neighborStates:
      break
    nextState = max(neighborStates, key = problem.heuristicFunc)
    if problem.heuristicFunc(nextState) <= problem.heuristicFunc(currentState):
      break
    currentState = nextState
  return currentState


def randomRestartHillClimbing(problem):
  count = 0
  state = problem.initialState()
  while count < 10 and problem.goalTest(state) == False:
    state = hillClimbing(problem)
    count += 1
  return state

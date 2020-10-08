import math
from ga import GeneticAlgorithm

function = lambda x, y : 4 * math.exp(-(x**2 + y**2 -2*(x+y-1))) + math.exp(-((x-3)**2+(y-3)**2)) + \
                            math.exp(-((x+3)**2+(y-3)**2)) + math.exp(-((x-3)**2+(y+3)**2)) + math.exp(-((x+3)**2+(y+3)**2))

print(function(2,3))

#path_planner = PathPlanner(5, 219, 'australia.csv')
#path_planner.grid.print_cities()

#path, cost = path_planner.a_star()
#print('Caminho: ')
#for city in path:
#    print(path_planner.agent_grid.cities[city.id - 1])
#print('Custo: ', cost)

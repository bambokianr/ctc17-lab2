import math
from ga import GeneticAlgorithm

num_generations = 2000
population_size = 100
crossover_prob = 0.25
mutation_prob = 0.1

function = lambda x, y : 4 * math.exp(-(x**2 + y**2 -2*(x+y-1))) + math.exp(-((x-3)**2+(y-3)**2)) + \
                            math.exp(-((x+3)**2+(y-3)**2)) + math.exp(-((x-3)**2+(y+3)**2)) + math.exp(-((x+3)**2+(y+3)**2))

genetic_algorithm = GeneticAlgorithm(function, population_size, crossover_prob, mutation_prob)
genetic_algorithm.generatePopulation()
genetic_algorithm.printPopulation()
for i in range(num_generations):
    genetic_algorithm.fitnessCalculation()
    genetic_algorithm.crossover()
    genetic_algorithm.mutation()
    genetic_algorithm.fitnessCalculation()
    genetic_algorithm.selectBestChromo()

    genetic_algorithm.printGeneration()

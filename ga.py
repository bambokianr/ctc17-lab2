from math import inf
import random
import struct

### ALGORTIMO GENETICO

# Agente para encontrar o menor caminho
class GeneticAlgorithm():
    def __init__(self, function, population_size, crossover_prob, mutation_prob):
        self.function = function
        self.population_size = population_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.best_chromosome = [0, 0, 0, 0] # x, y, fitness, position 
        self.population = []
        self.new_population = []
        self.fitness = []
        self.function_value = []
        self.generation = 0
        self.domain = 9

    def generatePopulation(self):
        for i in range(self.population_size):
            chromosome = []
            chromosome.append(random.uniform(-self.domain, self.domain))
            chromosome.append(random.uniform(-self.domain, self.domain))
            self.population.append(chromosome)

    def printPopulation(self):
        for i in range(self.population_size):
            print(self.population[i])

    def printFitness(self):
        for i in range(self.population_size):
            print(self.fitness[i])

    def printGeneration(self):
        self.generation += 1
        print()
        print('Generation: ', self.generation)
        print('Best global chromosome point: ', self.best_chromosome[0])
        print('Best global chromosome function value: ', self.best_chromosome[1])
        #print('Best global chromosome', self.best_chromosome)

    def selectBestChromo(self):
        best_chromo_temp = []
        best_function_value_temp = 0
        best_chromo_pos = 0
        find_best = False

        for i in range(self.population_size):
            if self.best_chromosome[1] < self.function_value[i]:
                best_chromo_temp = self.population[i]
                best_function_value_temp = self.function_value[i]
                best_chromo_pos = i
                find_best = True

        if (find_best):
            self.best_chromosome = []
            self.best_chromosome.append(best_chromo_temp)
            self.best_chromosome.append(best_function_value_temp)
            self.best_chromosome.append(best_chromo_pos)

    def floatToBits(self, f):
        s = struct.pack('>f', f)
        return struct.unpack('>l', s)[0]

    def bitsToFloat(self, b):
        s = struct.pack('>l', b)
        return struct.unpack('>f', s)[0]

    def fitnessCalculation(self):
        self.fitness = []
        self.function_value = []
        #print(len(self.population))
        for i in range(len(self.population)):
            #print(self.population[i][0])
            self.function_value.append(self.function(self.population[i][0], self.population[i][1]))
            #self.fitness.append(self.function(self.population[i][0], self.population[i][1]))

        #print(self.fitness)
        #print(self.function_value)
        sum_fitness = sum(self.function_value)
        for i in range(len(self.population)):
            if sum_fitness == 0:
                self.fitness.append(inf)
            else:
                self.fitness.append(self.function_value[i] / sum_fitness)

    # roleta
    def parentSelection(self):
        selection_number = random.random()
        selection_temp = 0

        #print(self.population)
        for i in range(len(self.population)):
            selection_temp += self.fitness[i]
            if selection_number < selection_temp:
                return i

    def crossover(self):
        self.new_population = []        
        pop_size_temp = self.population_size
        
        for i in range(round(pop_size_temp / 2)):
            parent_1_pos = self.parentSelection()
            parent_1 = self.population[parent_1_pos]
            self.population.pop(parent_1_pos)
            self.fitnessCalculation()
            parent_2_pos = self.parentSelection()
            parent_2 = self.population[parent_2_pos]
            self.population.pop(parent_2_pos)
            self.fitnessCalculation()

            #self.population.pop(parent_2_pos)

            #while (crossover_bool[parent_1_pos]):
            #    parent_1_pos = self.parentSelection()
            
            #while (parent_1_pos == parent_2_pos):
                #print(parent_1_pos, parent_2_pos)
            #    parent_2_pos = self.parentSelection()
            #print('alou')

            if (random.random() < self.crossover_prob):
                parent_1_x_hex = hex(self.floatToBits(parent_1[0]))
                parent_1_y_hex = hex(self.floatToBits(parent_1[1]))
                parent_2_x_hex = hex(self.floatToBits(parent_2[0]))
                parent_2_y_hex = hex(self.floatToBits(parent_2[1]))

                crosspoint = random.randint(3, 9)
                son_1_x_hex = ''
                son_1_y_hex = ''
                son_2_x_hex = ''
                son_2_y_hex = ''

                #print(parent_1_x_hex)
                #print(parent_1_y_hex)
                #print(parent_2_x_hex)
                #print(parent_2_y_hex)
                if (len(parent_1_x_hex) == 11):
                    son_1_x_hex += '-'
                    parent_1_x_hex = parent_1_x_hex.replace('-', '')
                if (len(parent_1_y_hex) == 11):
                    son_1_y_hex += '-'
                    parent_1_y_hex = parent_1_y_hex.replace('-', '')
                if (len(parent_2_x_hex) == 11):
                    son_2_x_hex += '-'
                    parent_2_x_hex = parent_2_x_hex.replace('-', '')
                if (len(parent_2_y_hex) == 11):
                    son_2_y_hex += '-'
                    parent_2_y_hex = parent_2_y_hex.replace('-', '')

                for i in range(10):
                    if (i < crosspoint):
                        son_1_x_hex += parent_1_x_hex[i]
                        son_1_y_hex += parent_1_y_hex[i]
                        son_2_x_hex += parent_2_x_hex[i]
                        son_2_y_hex += parent_2_y_hex[i]
                    else:
                        son_1_x_hex += parent_2_x_hex[i]
                        son_1_y_hex += parent_2_y_hex[i]
                        son_2_x_hex += parent_1_x_hex[i]
                        son_2_y_hex += parent_1_y_hex[i]
                #print(crosspoint)
                #print(son_1_x_hex)
                #print(son_1_y_hex)
                #print(son_2_x_hex)
                #print(son_2_y_hex)

                son_1_x = self.bitsToFloat(int(son_1_x_hex, 0))
                son_1_y = self.bitsToFloat(int(son_1_y_hex, 0))
                son_2_x = self.bitsToFloat(int(son_2_x_hex, 0))
                son_2_y = self.bitsToFloat(int(son_2_y_hex, 0))
                son_1 = []
                son_2 = []
                son_1.append(son_1_x)
                son_1.append(son_1_y)
                son_2.append(son_2_x)
                son_2.append(son_2_y)
                #print(son_1)
                #print(son_2)

                self.new_population.append(son_1)
                self.new_population.append(son_2)

                #print(len(self.population))

            else:
                self.new_population.append(parent_1)
                self.new_population.append(parent_2)
        
            #print(self.population)
            #self.population.pop(parent_1_pos)
            #self.population.pop(parent_2_pos)
            #self.fitness.pop(parent_1_pos)
            #self.fitness.pop(parent_2_pos)
    
        self.population = self.new_population

    def mutation(self):
        for i in range(self.population_size):
            if random.random() < self.mutation_prob:
                chromosome = []
                chromosome.append(random.uniform(-self.domain, self.domain))
                chromosome.append(random.uniform(-self.domain, self.domain))
                self.population.append(chromosome)

    def offspring(self):
        pass

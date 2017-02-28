import numpy as np

from domain.chromosome import Chromosome
from domain.gene import Gene
from services.fitness import FitnessCalculator
import random

number_of_drones = 5
map_seed = 123
calculator = FitnessCalculator(number_of_drones, map_seed)

delivery_items = calculator.get_delivery_items()

movements = ['N','W','S','E','P','D']

#BEGIN EXAMPLE
'''
genes = np.array([Gene(0, 'P', delivery_items[0]),
                  Gene(0, 'E'),
                  Gene(0, 'E'),
                  Gene(0, 'E'),
                  Gene(0, 'D', delivery_items[0]),
                  Gene(1, 'P', delivery_items[0]),
                  Gene(1, 'E'),
                  Gene(1, 'E'),
                  Gene(1, 'E'),
                  Gene(1, 'S'),
                  Gene(1, 'D', delivery_items[0]),
                  Gene(2, 'S'),
                  Gene(2, 'P', delivery_items[6]),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'D', delivery_items[6]),
                  Gene(3, 'P', delivery_items[1]),
                  Gene(3, 'S'),
                  Gene(3, 'P', delivery_items[2]),
                  Gene(3, 'S'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'D', delivery_items[2]),
                  Gene(3, 'D', delivery_items[1]),
                  Gene(4, 'P', delivery_items[5]),
                  Gene(4, 'S'),
                  Gene(4, 'P', delivery_items[5]),
                  Gene(4, 'S'),
                  Gene(4, 'S'),
                  Gene(4, 'S'),
                  Gene(4, 'E'),
                  Gene(4, 'D', delivery_items[5]),
                  Gene(4, 'D', delivery_items[5]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[4]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[4]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[3]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[3]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[3]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[3]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[3]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[3])])
'''

genes = []
#create genes for each drone
for droneIndex in range(0,5):
    #start with 3 mvoements per drone
    for mov in range(0, 3):
        currentMovement = movements[random.randint(0, 5)]
        if( currentMovement == 'P' or currentMovement == 'D'):
            index = random.randint(0, len(delivery_items) - 1)
            gene = Gene(droneIndex, currentMovement, delivery_items[index])
        else:
            gene = Gene(droneIndex, currentMovement)
        genes.append(gene)

genes = np.array(genes)

try:
    chromosome = Chromosome(genes)
    chromosomeFitness = calculator.get_fitness(chromosome)
    if(chromosomeFitness[1] == float('Inf')):
        print 'value is infinity'
    else:
        print chromosomeFitness
except:
    print "exception"
                
       
#print chromosomeFitness
#calculator.print_map()
#print "Chromosome Fitness [decimal percentage of items delivered, ratio of total distance traveled vs. map area]:", calculator.get_fitness(chromosome)

#END EXAMPLE



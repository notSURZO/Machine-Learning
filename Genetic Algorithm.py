import random





def generate_chromosome(n, slots):
  chromosome_list = []
  for j in range(10):
    chromosome = ''
    for i in range(n*slots):
      chromosome += str(random.randint(0,1))
    chromosome_list.append(chromosome)
  return chromosome_list


def fitnessCalc(n, chromosome):
  slot_consistency_penalty = 0
  slot_overlap_penalty = 0

  for i in range(0, len(chromosome), n):
    slot_string = chromosome[i:i+n]
    if slot_string.count('1') == 0 :
      slot_overlap_penalty += 0
    else:
      slot_overlap_penalty += slot_string.count('1') - 1

  for i in range(n):
    slot_index_one_count = 0
    for j in range(i, len(chromosome), n):
      if chromosome[j] == '1' :
        slot_index_one_count +=1
    slot_consistency_penalty += abs(slot_index_one_count - 1)
  total_penalty = slot_consistency_penalty + slot_overlap_penalty

  return -total_penalty



def singleCrossover(str_one, str_two):
  crossover_point = random.randint(0,len(str_one)-1)
  childOne = str_one[:(crossover_point)] + str_two[(crossover_point) :]
  childTwo = str_two[:(crossover_point)] + str_one[(crossover_point) :]
  return [childOne, childTwo]


def randomSelection(chromosomeList):
  chromosomeOne = chromosomeList[random.randint(0, len(chromosomeList)-1)]
  chromosomeTwo = chromosomeList[random.randint(0, len(chromosomeList)-1)]

  return [chromosomeOne, chromosomeTwo]


def mutation(childList):
  
  newChildList = []
  for i in range(len(childList)):
    mutated = ''
    toBeChanged = list(childList[i])
    numOfIndexChanged =  random.randint(0, len(toBeChanged))
    for i in range(numOfIndexChanged):
      toBeChanged[random.randint(0, len(toBeChanged)-1)] = str(random.randint(0,1))
    for j in toBeChanged:
      mutated += j
    newChildList.append(mutated)
  return newChildList





def geneticAlgorithm(n, t, initialPopulation):
  fitness = -99999999 
  
  while True :
    for i in initialPopulation:
      tempFitness = fitnessCalc(n, i)
      if tempFitness > fitness:
        fitness = tempFitness 
      if fitness == 0 :
        return (i, fitness) 
    randomlySelected = randomSelection(initialPopulation)
    offSprings = singleCrossover(randomlySelected[0], randomlySelected[1])
    mutatedOffSprings = mutation(offSprings)
    
    for i in mutatedOffSprings:
      initialPopulation[random.randint(0, (n*t)-1)] = i

inputFile = open("input.txt",'r')
values =  inputFile.readline().split()

n = int(values[0])
t = int(values[1])
initialPopulation = generate_chromosome(n,t)
result = geneticAlgorithm(n, t , initialPopulation)
print(result[0])
print(result[1])







def doubleCrossover(str_one, str_two):
  first_point = random.randint(0,len(str_one)-1)
  second_point = random.randint(0,len(str_one)-1)

  left_point = min(first_point, second_point)
  right_point = max(first_point, second_point)

  childOne = str_one[:left_point] + str_two[left_point : right_point] + str_one[right_point:]
  childTwo = str_two[:left_point] + str_one[left_point : right_point] + str_two[right_point:]
  return [childOne, childTwo]

 
random_selected = randomSelection(initialPopulation)
print("Double Crossover Parent 1:",random_selected[0])
print("Double Crossover Parent 2:",random_selected[1])
resultantOffsprings = doubleCrossover(random_selected[0], random_selected[1])
print("Double Crossover Offspring 1:",resultantOffsprings[0])
print("Double Crossover Offspring 2:",resultantOffsprings[1])
graphInputFile = open("22101349_Md Abu Tarabin Surzo_CSE422_05_Assignment01_Summer2024_InputFile.txt", "r") 
graphInputList = graphInputFile.readlines()
graphDict = {}
heuristics = {}
for k in range(len(graphInputList)):
  nodeInfoList = graphInputList[k].strip("\n").split(" ")
  heuristics[nodeInfoList[0]] = int(nodeInfoList[1])
  graphDict[nodeInfoList[0]] = []
  for i in range(2, len(nodeInfoList)-1, 2):
    graphDict[nodeInfoList[0]].append([nodeInfoList[i], int(nodeInfoList[i+1])])

def priority_sort(q):  #q would be like this- [['zerind', 75(f value)],['Timisora', 118],['Sibiu', 140]]
  tempDistanceList = []
  resultList = []
  for i in q:
    tempDistanceList.append(i[1]) #[75, 118, 140]
  tempDistanceList.sort()  
  for i in tempDistanceList:
    for j in q:
      if j[1] == i:
        resultList.append(j)
        tempDistanceList.remove(i)
  return resultList

def a_star(start, goal, graph ,heuristics):
  
  parentList = {}
  search_queue = [[start, heuristics[start]]]
  visited = []
  

  while len(search_queue)!=0:
  
    search_queue = priority_sort(search_queue)
    nodeWithLowestF = search_queue.pop(0) #[Bucharest, 418]
    visited.append(nodeWithLowestF[0])
    if nodeWithLowestF[0] == goal : #[Bucharest, 418]
      totalDistance = nodeWithLowestF[1]  
      currentNode = goal
      reversePath = [currentNode]
      while currentNode != start:
        reversePath.append(parentList[currentNode])
        currentNode = parentList[currentNode]    
      reversePath.reverse()
      return (totalDistance , reversePath)  
    neighborList =    graph[nodeWithLowestF[0]]
    currentG = nodeWithLowestF[1] - heuristics[nodeWithLowestF[0]]
    for neighbor in  neighborList:#neighbor --> [zerind, 75]
      if neighbor[0] not in visited: 
        neighborG = currentG + neighbor[1]
        neighborF = neighborG+heuristics[neighbor[0]]
        trigger = False
        for node in search_queue:
          if node[0] == neighbor[0] :
            trigger = True
            if node[1] > neighborF  :
              node[1] = neighborF
              
              
              parentList[neighbor[0]] = nodeWithLowestF[0]

        if trigger == False :
          search_queue.append([neighbor[0], neighborF])
          parentList[neighbor[0]] = nodeWithLowestF[0]

  if len(search_queue) == 0 :
      return  "NO PATH FOUND"


userGivenStart = input("Start node: ")
userGivenGoal =  input("Destination: ")
finalResult = a_star(userGivenStart, userGivenGoal, graphDict, heuristics)


if type(finalResult) == tuple: 
  pathString = ''
  for i in finalResult[1]:
    pathString+= i+" -> "
  path = pathString.strip("-> ")
  print(f'''Path: {path}
Total distance: {finalResult[0]} km''')
else:
  print(finalResult)

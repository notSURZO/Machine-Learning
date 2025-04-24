

# Part 1
print()
print('Part 1')
print()

import random

class Node:
    def __init__(self,utility=None):
        self.utility=utility
        self.children=[]


def tree(d):
    if d==0:
        return Node(random.choice([-1,1]))
    n=Node()
    n.children.append(tree(d-1))
    n.children.append(tree(d-1))
    return n

def alpha_beta_pruning(n,d,alpha,beta,max):
    if d==0 or n.utility != None:
        return n.utility
    if max == True:
        v = float('-inf')
        for i in n.children:
            vPrime = alpha_beta_pruning(i,d-1,alpha,beta,False)
            if vPrime > v :
              v = vPrime
            if vPrime >= beta :
              return v
            if vPrime > alpha :
              alpha = vPrime
        return v
    else:
        v = float('inf')
        for i in n.children:
            vPrime = alpha_beta_pruning(i,d-1,alpha,beta,True)
            if vPrime < v :
              v = vPrime
            if vPrime <= alpha :
              return v
            if vPrime < beta :
              beta = vPrime
        return v

def game(firstTurn):
    stateSpace=tree(5)
    scorpWin=0
    subWin=0
    winners = []

    for k in range(3):
        result = alpha_beta_pruning(stateSpace,5,float('-inf'),float('inf'),firstTurn==0)
        if result == -1:
            round_winner='Scorpion'
            scorpWin+=1
        else:
            round_winner='Sub-zero'
            subWin+=1
        winners.append(round_winner)
        if firstTurn==0:
            firstTurn = 1
        else:
            firstTurn = 0
    if scorpWin>subWin:
        print('Game Winner: Scorpion')
    else:
        print('Game Winner: Sub-zero')
    print('Total Rounds Played: 3')
    for i in range(3):
      print(f'Winner of Round {i+1}: {winners[i]}')


game(int(input("Select 0 or 1: ")))





# Part 2





class Node:

    def __init__(self,utility=None):
        self.utility=utility
        self.children=[]

u = [3,6,2,3,7,1,2,0]



def tree(d):

    if d==0:
        return Node(u.pop(0))
    node=Node()
    node.children.append(tree(d-1))
    node.children.append(tree(d-1))
    return node

def alpha_beta_pruning(node,d,alpha,beta,max):
    if d==0 or node.utility != None:
        return node.utility
    if max == True:
        v = float('-inf')
        for i in node.children:
            vPrime = alpha_beta_pruning(i,d-1,alpha,beta,False)
            if vPrime > v :
              v = vPrime
            if vPrime >= beta :
              return v
            if vPrime > alpha :
              alpha = vPrime
        return v
    else:
        v = float('inf')
        for i in node.children:
            vPrime = alpha_beta_pruning(i,d-1,alpha,beta,True)
            if vPrime < v :
              v = vPrime
            if vPrime <= alpha :
              return v
            if vPrime < beta :
              beta = vPrime
        return v

def game(c):
    scores = [3,6,2,3,7,1,2,0]
    stateSpace=tree(3)
    result_without_magic = alpha_beta_pruning(stateSpace,5,float('-inf'),float('inf'),True)

    result_with_magic = (max(max(scores[0:4]), max(scores[4:]))) - c

    if result_with_magic > result_without_magic :
      if max(scores[0:4]) > max(scores[4:]):
        print(f"The new minimax value is {max(result_without_magic, result_with_magic)}. Pacman goes left and uses dark magic")
      else:
        print(f"The new minimax value is {max(result_without_magic, result_with_magic)}. Pacman goes right and uses dark magic")
    else:
      print(f"The new minimax value is {max(result_without_magic, result_with_magic)}. Pacman does not use dark magic")

print()
print('Part 2')
print()
game(int(input("Select the value of c: ")))
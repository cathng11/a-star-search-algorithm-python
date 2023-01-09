from collections import defaultdict
from queue import PriorityQueue

data = defaultdict(list)
data['A'] = ['B', 2, 'C', 1, 'D', 3, 6]
data['B'] = ['E', 5, 'F', 4, 3]
data['C'] = ['G', 6, 'H', 3, 4]
data['D'] = ['I', 2, 'J', 4, 5]
data['E'] = [3]
data['F'] = ['K', 2, 'L', 1, 'M', 4, 1]
data['G'] = [6]
data['H'] = ['N', 2, 'O', 4, 2]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]


class Node:
    def __init__(self, name, par=None, g=0, h=0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h

    def __lt__(self, value):
        if value == None:
            return False
        return self.g+self.h < value.g+value.h

    def __eq__(self, value):
        if value == None:
            return False
        return self.name == value.name


def getPath(fr):
    print(fr.name,end=' ')
    temp = fr
    if temp.par != None:
        getPath(temp.par)
    else:
        return


def Astar(initialState, goalTest):
    frontier = PriorityQueue()
    explored = PriorityQueue()
    initialState.h = data[initialState.name][-1]
    frontier.put(initialState)

    while True:
        if frontier.empty() == True:
            print("Failed")
            return
        fr = frontier.get()
        explored.put(fr)
        print(">> ", fr.name, fr.g, fr.h)

        if fr == goalTest:
            print("Success!")
            getPath(fr)
            print("\nCost: ", (fr.g+fr.h))
            return
        i = 0
        while i < len(data[fr.name])-1:
            name = data[fr.name][i]
            g = fr.g+data[fr.name][i+1]
            h = data[name][-1]
            tmp = Node(name=name, g=g, h=h)
            tmp.par = fr

            if not (tmp in frontier.queue) and not (tmp in explored.queue):
                frontier.put(tmp)
            i += 2


Astar(Node('A'), Node('N'))

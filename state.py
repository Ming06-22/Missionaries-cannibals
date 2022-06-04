import cross_river
# State (Missionaries, Cannibals, BoatA, BoatB)
class State:
    def __init__(self, m, c, a, b):
        self.m = m  # The number of Missionaries on the right side
        self.c = c  # The number of Cannibals on the right side
        self.a = a  # a = 1: BoatA on the right side; a = 0: BoatA on the left side
        self.b = b  # b = 1: BoatB on the right side; b = 0: BoatB on the left side
        self.num = 0
        self.parent = None
        self.g = 0                      # g(x)
        self.h = 0                      # h(x)
        self.f = self.g + self.h  # f(x) = g(x) + h(x)
        self.boat = BoatState(0, 0, 0, 0)
        self.cost = 0
    def display(self):
        print(f"{self.m:<11}{self.c:<9}{self.a:<7}{self.b:<7}", end = "")
        print(self.boat.node)

class BoatState:
    def __init__(self, am, ac, bm, bc):
        self.am = am  # The number of Missionaries on BoatA
        self.ac = ac  # The number of Cannibals on BoatA
        self.bm = bm  # The number of Missionaries on BoatB
        self.bc = bc  # The number of Cannibals on BoatB
        self.node = [am, ac, bm, bc]

# Determine whether the state reach the goal
def isGoal(x):
    if x.m == 0 and x.c == 0 and (x.a == 0 or x.b == 0):
        return True
    else:
        return False

# Determine whether the state is in the Open List
def inOpen(x, open):
    for e in open:
        if x.m == e.m and x.c == e.c and x.a == e.a and x.b == e.b:
            return True
    return False

# Determine whether the state is legal
def isLegal(bank, boat):
    flag1 = flag2 = flag3 =  False
    if bank.m >= 0 and bank.m <= M and bank.c >= 0 and bank.c <= C:
        if bank.m == 0 or bank.m >= bank.c:
            flag1 = True

    if boat.am >= boat.ac and boat.bm >= boat.bc:
        flag2 = True

    if M - bank.m >= C - bank.c:
        flag3 = True

    return flag1 and flag2 and flag3

# Heuristic funtion
def h(s):
    if cross_river.version == 1 or cross_river.version == 3:
        tmp = s.m + s.c - 2 * s.a - 3 * s.b
        if tmp >= 0:
            return tmp
        else:
            return 0
    else:
        return 0

# conclude the closed_list to result
def showResult(list):
    result = []
    temp = list[-1]
    result.append(temp)
    while True:
        for e in list:
            if e.num == temp.parent:
                temp = e
                break
        result.append(temp)
        if temp.num == 0:
            break
    return result
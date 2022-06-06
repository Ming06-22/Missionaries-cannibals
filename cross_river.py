import logging
import os
import state
import sys
import time

A = 2  # Capacity of BoatA
B = 3  # Capacity of BoatB
number = 1

# Expand node
def addChild(list, current):
    global number
    # when both boat are on the right bank
    if current.a == True and current.b == True:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                next_state = state.State(current.m - a2, current.c - (a1 - a2), not current.a, current.b)
                next_state.g = current.g + A_COST
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_a
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1 + 1):
                next_state = state.State(current.m - b2, current.c - (b1 - b2), current.a, not current.b)
                next_state.g = current.g + B_COST
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_b
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m - a2 - b2, current.c - (a1 - a2) - (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + AB_COST
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        next_state.cost = current.cost + cost_adder_ab
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

    # when boatA is on the right bank and boatB is on the left bank
    if current.a == True and current.b == False:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                next_state = state.State(current.m - a2, current.c - (a1 - a2), not current.a, current.b)
                next_state.g = current.g + A_COST
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_a
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)
                    
        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1 + 1):
                next_state = state.State(current.m + b2, current.c + (b1 - b2), current.a, not current.b)
                next_state.g = current.g + B_COST
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_b
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)
        
        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m - a2 + b2, current.c - (a1 - a2) + (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + AB_COST
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        next_state.cost = current.cost + cost_adder_ab
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

    # when boatA is on the left bank and boatB is on the right bank
    if current.a == False and current.b == True:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                next_state = state.State(current.m + a2, current.c + (a1 - a2), not current.a, current.b)
                next_state.g = current.g + A_COST
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_a
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1 + 1):
                next_state = state.State(current.m - b2, current.c - (b1 - b2), current.a, not current.b)
                next_state.g = current.g + B_COST
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_b
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)
        
        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m + a2 - b2, current.c + (a1 - a2) - (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + AB_COST
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        next_state.cost = current.cost + cost_adder_ab
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

    # when both boats are on the left bank
    if current.a == False and current.b == False:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1):
                next_state = state.State(current.m + a2, current.c + (a1 - a2), not current.a, current.b)
                next_state.g = current.g + A_COST
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_a
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1):
                next_state = state.State(current.m + b2, current.c + (b1 - b2), current.a, not current.b)
                next_state.g += current.g + B_COST 
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                next_state.cost = current.cost + cost_adder_b
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m + a2 + b2, current.c + (a1 - a2) + (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + AB_COST
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        next_state.cost = current.cost + cost_adder_ab
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

if __name__ == '__main__':
    print("(1) A* search base on money cost")
    print("(2) A* search base on time cost")
    print("(3) Uniform cost search base on money cost")
    print("(4) Uniform cost search base on time cost\n")
    while(True):
        state.version = input("Please enter the version number:")
        if state.version in ["1", "2", "3", "4"]:
            break
        else:
            print("Please enter one to four.\n")
    state.M = int(input("Please enter the amount of missionary:"))
    state.C = int(input("Please enter the amount of cannibal:"))
    limit = int(input("Please enter the limit:"))
    if state.version == "1" or state.version == "3":
        A_COST = 3
        B_COST = 25
        AB_COST = 28
        cost_adder_a = 1
        cost_adder_b = 1
        cost_adder_ab = 1
    else:
        A_COST = B_COST = AB_COST = 1
        cost_adder_a = 3
        cost_adder_b = 25
        cost_adder_ab = 28
    timeStart = time.time()
    open_list = []
    closed_list = []
    result = False

    init = state.State(state.M, state.C, True, True)
    goal = state.State(0, 0, False, False)  # the last two elements are not important

    open_list.append(init)
    
    # check whether the initial state is legal
    if (not (state.isLegal((init), state.BoatState(1, 1, 0, 0)))):
        print("The condition doesn't have a solution.")
        sys.exit()

    # Build log file
    filename = f'{state.M}-{state.C}.log'
    if os.path.isfile(filename):
        os.remove(filename)
    log = logging.getLogger()

    handler = logging.FileHandler(filename = filename) 
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    
    while(len(open_list) != 0):
        current_state = open_list.pop(0)
        closed_list.append(current_state)
        if state.isGoal(current_state):
            result = True
            break
        
        children = []
        addChild(children, current_state)

        for child in children:
            if state.inOpen(child, open_list):
                for e in open_list:
                    if e.m == child.m and e.c == child.c and e.a == child.a and child.b == child.b:
                        if child.g < e.g:
                            e = child
                        break
            elif child.cost <= limit:
                open_list.append(child)

        # order open_list with the key: f(x) and cost(h(x) small and cost small -> forward)
        open_list = sorted(open_list, key = lambda x: x.h)
        open_list = sorted(open_list, key = lambda x: x.f)

        # write log file
        log.debug("OpenList:")
        for e in open_list:
            log.debug(f"{e.num: <5} -> [{e.m},{e.c},{e.a},{e.b}], Parent={e.parent}")
        log.debug("ClosedList:")   
        for e in closed_list:
            log.debug(f"{e.num: <5} -> [{e.m},{e.c},{e.a},{e.b}], Parent={e.parent}")
        log.debug("")
    timeEnd = time.time()
    
    if result == True:
        print("-" * 50)
        print("Missionary Cannibal Boat_A Boat_B state")
        answer = state.showResult(closed_list)
        answer = reversed(answer)
        # write log file
        log.debug(f"Solution (Cost = {closed_list[-1].g}) :")
        for e in answer:
            if e.parent != None:
                log.debug(f"[{e.boat.am},{e.boat.ac},{e.boat.bm},{e.boat.bc}]") 
            log.debug(f"{e.num: <5} -> [{e.m},{e.c},{e.a},{e.b}]")
            e.display()
        print("-" * 50)
        print("Total cost = ", closed_list[-1].g, ", total nodes = ", len(open_list) + len(closed_list))
        print("Time: ", str(round(timeEnd - timeStart, 2)), "sec")
    else:
        print("The condition doesn't have a solutiion.")
import gymnasium
import numpy as np

def dividable(x, y):
    return y != 0 and x % y == 0

def step(a: list[int], i: int, j: int, op: int):
    t = 0
    match op:
        case 0:
            t = a[i] + a[j]
        case 1:
            t = a[i] - a[j]
        case 2:
            t = a[i] * a[j]
        case 3:
            t = a[i] // a[j]
    
    if i > j:
        i, j = j, i
    return [t] + a[0:i] + a[i+1:j] + a[j+1:]

solve_count = 0

def solve(a: list[int], r: int, actions: list[tuple[int, int, int]]):
    global solve_count
    solve_count += 1
    if solve_count % 1000000 == 0:
        print(f"solve_count = {solve_count}")
    l = len(a)
    if l == 1:
        return a[0] == r
    else:
        for i in range(0, l):
            for j in range(i+1, l):
                if solve(step(a, i, j, 0), r, actions):
                    actions.append((i, j, 0))
                    return True
                if a[i] >= a[j] and solve(step(a, i, j, 1), r, actions):
                    actions.append((i, j, 1))
                    return True
                if a[j] >= a[i] and solve(step(a, j, i, 1), r, actions):
                    actions.append((j, i, 1))
                    return True
                if solve(step(a, i, j, 2), r, actions):
                    actions.append((i, j, 2))
                    return True
                if dividable(a[i], a[j]) and solve(step(a, i, j, 3), r, actions):
                    actions.append((i, j, 3))
                    return True
                if dividable(a[j], a[i]) and solve(step(a, j, i, 3), r, actions):
                    actions.append((j, i, 3))
                    return True
    return False

OP_MAP = ['+', '-', '*', '/']

def test(a: list[int], r: int):
    actions = []
    print("问：{} 算 {}...".format(a, r))
    if solve(a, r, actions):
        print("答：找到解法了：")
        for i, j, op in reversed(actions):
            print(f"{a[i]} {OP_MAP[op]} {a[j]}")
            a = step(a, i, j, op)
            print(f"=> {a}")
    else:
        print("答：找不到解法")

class SimpleAgent:
    def predict(self, observation: list[int]) -> list[int]:
        pass

#test([1, 5, 7, 17, 45, 2], 24)

a = np.random.random_integers(0, 1000, 100).tolist()

test(a, 24)
print(f"solve_count = {solve_count}")

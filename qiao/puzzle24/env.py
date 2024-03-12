import gymnasium
from gymnasium import spaces

def dividable(x: int, y: int):
    return y != 0 and x % y == 0

def reduce_numbers(numbers:list[int], index1:int, index2:int, r:int):
    return [r] + numbers[0:index1] + numbers[index1+1:index2] + numbers[index2+1:]

class Puzzle24Env(gymnasium.Env):
    MAX_VALUE = 100

    def __init__(self, max_len: int) -> None:
        self.observation_space = spaces.Discrete(max_len + 1)   # number sequence + expected result
        # 操作数1， 操作数2，操作符（+，-，*，/）
        self.action_space = spaces.Discrete(3)

        self.__max_len = max_len
        self.__numbers: list[int] = None
        self.__expected: int = 0

    def __get_observation(self):
        return self.__numbers + [self.__expected]
    
    def __get_info(self):
        return {}

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self.__numbers = self.np_random.integers(0, Puzzle24Env.MAX_VALUE, self.__max_len)
        self.__expected = self.np_random.integers(0, Puzzle24Env.MAX_VALUE)

        return self.__get_observation(), self.__get_info()
    
    def step(self, action):
        index1 = action[0]
        index2 = action[1]
        op = action[2]

        n1 = self.__numbers[index1]
        n2 = self.__numbers[index2]

        r = -1
        if op == 0:
            r = n1 + n2
        elif op == 1:
            r = n1 - n2 if n1 >= n2 else n2 - n1
        elif op == 2:
            r = n1 * n2
        elif op == 3:
            if dividable(n1, n2):
                r = n1 / n2
            elif dividable(n2, n1):
                r = n2 / n1
            else:
                r = -1
        
        if r >= 0:
            self.__numbers = reduce_numbers(self.__numbers, index1, index2, r)

        terminated = len(self.__numbers) == 1 and self.__numbers[0] == self.__expected
        reward = 1 if terminated else 0
        
        return self.__get_observation(), reward, terminated, False, self.__get_info()

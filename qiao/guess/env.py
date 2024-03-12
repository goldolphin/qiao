import random

LOWER = 0
UPPER = 1024

class GuessGame:
    def __init__(self) -> None:
        self.__answer: int = random.randint(LOWER, UPPER)
    
    def guess(self, number: int):
        if number == self.__answer:
            return 0
        elif number < self.__answer:
            return -1
        else:
            return 1


NumberType = list[int]

ObsType = tuple[int, list[int]]
ActionType = tuple[int, int]

class GuessEnv:
    def step(self, action: ActionType) -> tuple[ObsType, float, bool]:
        opcode, operand = action
        op = OP_TABLE[opcode]

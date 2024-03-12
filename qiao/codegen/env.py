
class Calculator:
    def __init__(self) -> None:
        self.__stack: list[int] = []

    def load(self, ):
        pass

    def add():
        pass
    def sub():
        pass
    def mul():
        pass
    def div():
        pass


OP_TABLE = [
    Ops.load,
    Ops.add,
    Ops.sub,
    Ops.mul,
    Ops.div,
]

OPERAND_TABLE = list(range(10))

ObsType = tuple[int, list[int]]
ActionType = tuple[int, int]

class SimpleFunctionENv:
    def step(self, action: ActionType) -> tuple[ObsType, float, bool]:
        opcode, operand = action
        op = OP_TABLE[opcode]


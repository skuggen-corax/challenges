# from https://gitlab.com/scul/Advent-of-Code-2019

from typing import Union
from collections import defaultdict


class IntCode:
    def __init__(self, mem, input, i=-1):
        self.i = i
        self.mem = defaultdict(int, enumerate(map(int, mem)))
        self.rb = 0
        self.ip = 0
        self.op = -1
        self.modes = []
        self.reads = []
        self.writes = []
        self.input = input
        self.halted = False
        self.paused = False

    def _get_inst(self) -> None:
        mem = str(self.mem[self.ip]).zfill(5)
        self.op = int(mem[-2:])
        self.modes = [int(c) for c in mem[:-2][::-1]]

    def _get_args(self, size: int) -> None:
        args = [self.mem[self.ip + i] for i in range(1, size)]
        self.reads = [(self.mem[x], x, self.mem[x + self.rb])[m] for x, m in zip(args, self.modes)]
        self.writes = [(x, None, x + self.rb)[m] for x, m in zip(args, self.modes)]

    # def input(self, inp):
    #     if type(inp) == int:
    #         self.inputs.append(inp)
    #         self.paused = False
    #     elif type(inp) == list:
    #         for v in inp:
    #             self.inputs.append(v)
    #         self.paused = False

    def run_all(self):
        ans = []
        while True:
            val = self.run()
            if val is None:
                return ans
            ans.append(val)

    def run(self) -> Union[None, int]:
        """Returns next output"""
        while True:
            self._get_inst()
            if self.op == 99:  # Halt
                self.halted = True
                return None

            size = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2][self.op]
            self._get_args(size)

            self.ip += size
            if self.op == 1:  # Add
                self.mem[self.writes[2]] = self.reads[0] + self.reads[1]

            elif self.op == 2:  # Multiply
                self.mem[self.writes[2]] = self.reads[0] * self.reads[1]

            elif self.op == 3:  # Input
                if self.i == -1:
                    inp = self.input()
                else:
                    inp = self.input(self.i)
                if type(inp) == int:
                    inp = [inp]
                self.mem[self.writes[0]] = inp.pop(0)

            elif self.op == 4:  # Output
                return int(self.reads[0])

            elif self.op == 5:  # Jump if Not Zero
                if self.reads[0]:
                    self.ip = self.reads[1]

            elif self.op == 6:  # Jump if Zero
                if not self.reads[0]:
                    self.ip = self.reads[1]

            elif self.op == 7:  # Less Than
                self.mem[self.writes[2]] = (self.reads[0] < self.reads[1])

            elif self.op == 8:  # Equals
                self.mem[self.writes[2]] = (self.reads[0] == self.reads[1])

            elif self.op == 9:  # Relative Base
                self.rb += self.reads[0]

            else:
                print(f'Unhandled error on code: {self.op}\nip = {self.ip}\nmem = {self.mem}')
                assert False


def tests():
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    for i in [7, 8, 9]:
        vm = IntCode(program, lambda: i)
        vm.input()
        output = vm.run()
        assert (output == (i == 8))

    program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    for i in [7, 8, 9]:
        vm = IntCode(program, lambda: i)
        vm.input()
        output = vm.run()
        assert (output == (i < 8))

    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    for i in [7, 8, 9]:
        vm = IntCode(program, lambda: i)
        vm.input()
        output = vm.run()
        assert (output == (i == 8))

    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    for i in [7, 8, 9]:
        vm = IntCode(program, lambda: i)
        vm.input()
        output = vm.run()
        assert (output == (i < 8))

    for i in [0, 1, -2]:
        program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        vm = IntCode(program, lambda: i)
        vm.input()
        output = vm.run()
        assert (output == (i != 0))

        program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        vm = IntCode(program, lambda: i)
        vm.input()
        output = vm.run()
        assert (output == (i != 0))

    program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
               20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    a = {7: 999, 8: 1000, 9: 1001}
    for i in [7, 8, 9]:
        vm = IntCode(program, lambda: i)
        vm.input()
        output = vm.run()
        # print(output)
        assert output == a[i]
    print('tests passed')


if __name__ == '__main__':
    tests()

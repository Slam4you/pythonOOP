class ExtendedStack(list):
    def sum(self):
        if len(self) >= 2:
            x1 = self.pop()
            x2 = self.pop()
            self.append(x1 + x2)

    def sub(self):
        if len(self) >= 2:
            x1 = self.pop()
            x2 = self.pop()
            self.append(x1 - x2)

    def mul(self):
        if len(self) >= 2:
            x1 = self.pop()
            x2 = self.pop()
            self.append(x1 * x2)

    def div(self):
        if len(self) >= 2:
            x1 = self.pop()
            x2 = self.pop()
            self.append(x1 // x2)

ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
print(ex_stack)
ex_stack.sum()
print(ex_stack)
ex_stack.sub()
print(ex_stack)
ex_stack.mul()
print(ex_stack)
ex_stack.div()
print(ex_stack)
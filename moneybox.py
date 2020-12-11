class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.val = 0

    def can_add(self, v):
        self.v = v
        if self.val + self.v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if x.can_add(v):
            self.val += v

x = MoneyBox(14)
while True:
    x.add(int(input('How much to add?')))
    print(x.val)
class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x < 1:
            raise NonPositiveError
        else:
            super(PositiveList, self).append(x)


mlist = PositiveList()
print(mlist)
mlist.append(22)
print(mlist)

